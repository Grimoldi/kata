# Theatrical Players Kata

Kata taken from the [Theatrical Players Kata by Emily Bache](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata).

--------
Theatrical Players Requirements Specification

Refactoring is usually driven by a need to make changes.

In the book, Fowler adds code to print the statement as HTML in addition to the existing plain text version.

He also mentions that the theatrical players want to add new kinds of plays to their repertoire, for example history and pastoral.

--------
This project uses [pytest](https://docs.pytest.org/en/latest/) and [approvaltests](https://github.com/approvals/ApprovalTests.Python). Pytest is configured in the file 'pytest.ini'. See also [documentation for pytest-approvaltests](https://pypi.org/project/pytest-approvaltests/).

## Main Goal

While threating every kata as an _ad hoc_ library, the main goal is to implement the new requirements without breaking previous usage/integrations of the library itself.

For this reason the function retains its old signature, apart from optional parameters that aim to implement the new functionalities.

The only way to be sure that the old functionality has been preserved is with the default tests, verifying that it doesn't change and that the exception is still raised with the old Exception type and for the same reason (apart from changing the play type of course.)
