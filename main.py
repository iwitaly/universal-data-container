def check_all_elements_have_the_same_property(array, func):
    if len(array) == 0:
        return
    first_element_type = func(array[0])
    do_all_have_property = all(func(x) == first_element_type
                                for x in array)

    return do_all_have_property


class Series(object):
    def __init__(self, array):
        self._array = array
        if len(array) == 0:
            return
        is_homogeneous = check_all_elements_have_the_same_property(array,
                                                                   type)
        if not is_homogeneous:
            raise ValueError('Non homogeneous array')

        first_element_type = type(array[0])
        self._type = first_element_type


    def get_element(self, idx):
        if idx >= self.size():
            raise IndexError()

    def size(self):
        return len(self._array)


    def __len__(self):
        return len(self._array)


    def __str__(self):
        return '{} {}'.format(self._array, self._type)



class DataFrame(Series):
    def __init__(self, d):
        if type(d) == dict:
            array = d.values()
        else:
            array = d
        super(DataFrame, self).__init__(array)
        all_the_same_len = check_all_elements_have_the_same_property(array,
                                                                     len)
        if not all_the_same_len:
            raise ValueError('Not all elements have the same len')

        if type(d) == dict:
            self.columns = d

        del self._type

    def __str__(self):
        return '{}'.format(self._array)