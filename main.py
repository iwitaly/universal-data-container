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
        if idx >= self.get_size():
            raise IndexError()

    def get_size(self):
        return len(self._array)

    def get_type(self):
        return self._type

    def __len__(self):
        return len(self._array)

    def __str__(self):
        return '{} {}'.format(self._array, self._type)



class DataFrame(Series):
    def __init__(self, d):
        if type(d) != dict:
            d = {
                i: d[i]
                for i in range(len(d))
            }
        array = list(d.values())

        super(DataFrame, self).__init__(array)
        all_the_same_len = check_all_elements_have_the_same_property(array,
                                                                     len)
        if not all_the_same_len:
            raise ValueError('Not all elements have the same len')

        if type(d) == dict:
            self._columns = d

        del self._type


    def get_columns(self):
        return list(self._columns.keys())


    def get_column(self, column_name):
        column = self._columns.get(column_name)
        if column is None:
            error_message = 'No such a column {}. Avalable columns {}'.format(column_name,
                                                                             self.get_columns())
            raise KeyError(error_message)
        return column


    def filter_by_type(self, instance_type):
        return [
            x for x in self._array
            if x.get_type() == instance_type
        ]


    def get_row(self, ind):
        if ind >= self.get_size():
            raise IndexError()




    def del_column(self, column_name):
        raise NotImplemented()


    def del_row(self, ind):
        raise NotImplemented()


    def __str__(self):
        return '{}'.format(self._columns)