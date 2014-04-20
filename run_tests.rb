class String
def red;            "\033[31m#{self}\033[0m" end
def green;          "\033[32m#{self}\033[0m" end
end

require 'open3'

tests = Dir.glob("**/test_*")
wd    = Dir.pwd

tests.each do |test|
  Dir.chdir(File.dirname(test))
  stdout, stderr, _ = Open3.capture3(%{python "#{File.basename(test)}"})
  Dir.chdir(wd)
  File.open('results', 'a') { |f| f.write(test + "\n" + stdout + stderr) }
end

def find_number_of_tests(filename)
  sum = 0
  File.readlines(filename).each do |line|
    if line.match(/Ran \d tests/)
      sum += line[/\d+/].to_i
    end
  end
  sum
end

if not File.read('results').include?('FAILED')
  number = find_number_of_tests('results')
  puts "All #{number} tests passed.".green
else
  print File.read('results').red
end

system("rm results")
