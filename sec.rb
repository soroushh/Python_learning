class Person

  attr_reader :name, :family
  def initialize(name, family)
    @name = name
    @family = family
  end

  def full_name
    return(@name + " " + @family)
  end

end

person = Person.new("soroush","khosravi")

puts(person.full_name())
