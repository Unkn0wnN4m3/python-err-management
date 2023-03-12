from my_exceptions import CustomError1, CustomError2, CustomError3

raise ExceptionGroup(
    'My errors group',
    [CustomError1(), CustomError2(),
     CustomError3()])
