tests = Dir.glob("**/test_*")
wd = Dir.pwd

tests.each do |test|
  puts "### Running tests for #{test}"
  Dir.chdir(File.dirname(test))
  system("python #{File.basename(test)}")
  Dir.chdir(wd)
  puts "\n\n"
end
