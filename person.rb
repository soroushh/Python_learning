class Person
  def initialize(name , family)
    @name = name
    @family = family
  end

  def full_name()
    return(" the full name is "+ @name + " "+ @family)
  end
end 
