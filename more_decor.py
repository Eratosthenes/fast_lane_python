def beg(target_fun):
  def wrapper(*args):
    msg, say_please = target_fun(*args)
    if say_please:
      return "{} {}".format(msg,"Please! I am poor :(")
    return msg

  return wrapper

@beg
def say(say_please=False):
  msg="Can you buy me a beer?"
  return msg, say_please



