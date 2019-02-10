require "json"

py_src = STDIN.read

name_id_matches = py_src.scan(/pretty_name="(.+)"|mtga_id=(\d+)/)

id_name_pairs = name_id_matches.each_slice(2).map { |name_arr, id_arr|
  [Integer(id_arr.last), name_arr.first]
}

json = JSON.dump(Hash[id_name_pairs])

STDOUT.puts json
