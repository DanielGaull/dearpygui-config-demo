# Return a new string that is _str padded with spaces, if necessary until it is
# at least _len characters long
def right_pad_str(_str, _len):
  return _str + " " * max(0, _len - len(_str))

# Given a group a strings, finds the longest string and returns a dictionary
# mapping each string in the original group to a version of itself that is
# padded to be as long as the longest string in the original group.
def justify_str_group(*strs):
  justified = {}

  max_len_in_group = 0
  for _str in strs:
    if len(_str) > max_len_in_group:
      max_len_in_group =  len(_str)
  for _str in strs:
    justified[_str] = right_pad_str(_str, max_len_in_group)

  return justified