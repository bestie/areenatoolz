require "spec_helper"
require "nokogiri"
require "json"

class ArenaLog
  include Enumerable

  def initialize(html)
    @html = html
  end

  attr_reader :html
  private     :html

  def find_by(criteria)
    each_json.find { |entry|
      criteria.all? { |key, value|
        entry[key] == value
      }
    }
  end

  def each(&block)
    entries.each(&block)
  end

  def each_json(&block)
    entries.lazy.map { |e| parse_json_entry(e) }
  end

  private

  def entries
    @entries ||= html.css("div.log-row")
  end

  def parse_json_entry(entry)
    return {} unless entry.text.include?("{")

    JSON.parse(entry.text.lines.drop(1).join("\n"))
  rescue JSON::ParserError => _e
    {}
  end
end


RSpec.describe "What is even in these logs?" do
  let(:raw_html) { File.read("sample_logs/Log - 09-02-2019 11.13.35 - 1.htm") }
  let(:nokogiri_log_doc) { Nokogiri::HTML(raw_html) }

  let(:card_lookup) {
    JSON.parse(File.read("grpIds.json"))
  }

  let(:log) {
    ArenaLog.new(nokogiri_log_doc)
  }

  it "has lots of divs that you might assume have logs in them" do
    expect(log.count).to eq(3000)
  end

  it "starts to get interesting about 18 entries down" do
    entry = log.each_json.to_a[17]

    expect(entry).to include(
      "ClientToMatchServiceMessageType" => 2,
      "TransactionId" => "7c7e9d69-f1ad-4f7f-a6d4-a9c4456f6dd3",
    )
  end

  it "sets up zones - Battle field is always 28 I guess" do
    entry = log.find_by(
      "transactionId" => "65659717-0de3-4ba6-9063-62eab2738498"
    )

    expect(entry).to include(
      "greToClientEvent" => hash_including(
        "greToClientMessages" => include(
          hash_including(
            "type" => "GREMessageType_GameStateMessage",
            "gameStateMessage" => hash_including(
              "zones" => include(
                hash_including(
                  "zoneId" => 28,
                  "type" => "ZoneType_Battlefield",
                  "visibility" => "Visibility_Public",
                )
              )
            )
          )
        )
      )
    )
  end

  DATA = [{
    "grpId" => 1,
    "more" => {
      "grpId" => 2,
      "more" => {
        "grpId" => 3,
      }
    }
  }
  ]

  it "has some logs with grpIds, these refer to cards" do
    grpIds = find_grp_ids(log.each_json.take(50))

    expect(grpIds).to eq([
      66489,
      68667,
      68740,
      67017,
      68613,
      68734,
      68734,
      67019,
      66889,
      67266,
      67266
    ])

    expect(grpIds.map { |id| card_lookup.fetch(id.to_s) }).to eq([
      "Glacial Fortress",
      "Thought Erasure",
      "Watery Grave",
      "Island",
      "Assassin's Trophy",
      "Overgrown Tomb",
      "Overgrown Tomb",
      "Swamp",
      "Jadelight Ranger",
      "Cast Down",
      "Cast Down",
    ])
  end

  it "has some logs with grpIds, these refer to cards" do
    cards = find_grp_ids(log.each_json).map { |id| [id, card_lookup.fetch(id.to_s, "CARD NOT FOUND")] }

    File.open("game.txt", "w") do |f|
      cards.each { |id, name| f.write([id, name].join(",") + "\n") }
    end
  end

  it "has some logs with grpIds, these refer to cards" do
    expect(find_grp_ids(DATA)).to eq([1,2,3])
  end


  def find_grp_ids(data)
    data.flat_map { |k, v|
      if k.respond_to?(:each)
        find_grp_ids(k)
      elsif v.respond_to?(:each)
        find_grp_ids(v)
      elsif k == "grpId"
        [v]
      else
        []
      end
    }.to_a
  end
end
