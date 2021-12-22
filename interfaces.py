from abc import ABC, abstractmethod


class ICourse(ABC):
    """Interface for Course """

    @abstractmethod
    def __init__(self, title, teacher, list_of_topics):
        pass

    @property
    @abstractmethod
    def title(self):
        """Get the name of course."""
        pass

    @title.setter
    @abstractmethod
    def title(self, title):
        """Set the name of course."""
        pass

    @property
    @abstractmethod
    def teacher(self):
        """Get the teacher of course."""
        pass

    @teacher.setter
    @abstractmethod
    def teacher(self, teacher):
        """Set the teacher of course."""
        pass


class ILocalCourse(ABC):
    """Interface for ILocalCourse """

    @abstractmethod
    def __init__(self, title, teacher, list_of_topics):
        pass

    @abstractmethod
    def __str__(self):
        pass


class IOffsiteCourse(ABC):
    """Interface for IOffsiteCourse """

    @abstractmethod
    def __init__(self, title, teacher, list_of_topics):
        pass

    @abstractmethod
    def __str__(self):
        pass


class ITeacher(ABC):
    """Interface for Teacher """

    @abstractmethod
    def __init__(self, name, name_course=None):
        pass

    @property
    @abstractmethod
    def name(self):
        """Get the teacher's name of course."""
        pass

    @name.setter
    @abstractmethod
    def name(self, name):
        """Set the teacher's name of course."""
        pass

    @property
    @abstractmethod
    def name_course(self):
        """Get the list of course."""
        pass

    @name_course.setter
    @abstractmethod
    def name_course(self, name_courses):
        """Set the list of course."""
        pass

    @abstractmethod
    def __str__(self):
        pass


class ICourseFactory(ABC):
    """Interface for ICourseFactory """

    @abstractmethod
    def add_teacher(self, name, course=None):
        """Return object of Teacher class. Create teacher and write it to json . """
        pass

    @abstractmethod
    def add_course(self, title, teacher, list_of_topics, type_course):
        """Return object of Course class. Create course and write it to json ."""
        pass

    @abstractmethod
    def del_teacher(self, name, title):
        """Return update dictionary of teachers. Delete teacher from course."""
        pass
