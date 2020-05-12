def convert_units(value_to_be_converted, units_of_the_value_to_be_converted_from):

        #:param value_to_be_converted: Somevalue
        #:param units_of_the_value_to_be_converted_from: Accepted units: cb/a, rb/a, rb/cb
        #:param units_to_be_converted_to: Accepted units: ca/a, ev/a, ggp
        #:return: value_in_the_requested_units

    if units_of_the_value_to_be_converted_from == "cb/a":
        value_in_the_requested_units = value_to_be_converted * 0.148185
    elif units_of_the_value_to_be_converted_from == "rb/a":
        value_in_the_requested_units = value_to_be_converted * 13.6057
    elif units_of_the_value_to_be_converted_from == "rb/cb":
        value_in_the_requested_units = value_to_be_converted / 29421.02648438959
    else:
        value_in_the_requested_units = value_to_be_converted
    return value_in_the_requested_units