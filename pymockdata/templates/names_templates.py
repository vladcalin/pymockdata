from pymockdata.core.base.template import Template


class FullMaleNameTemplate(Template):
    pattern_list = [
        "{male_name} {last_name}",
        "{male_name} {last_name}",
        "{male_name} {last_name}",
        "{male_name} {last_name}",
        "{male_name} {last_name}",

        "{male_name}-{male_name} {last_name}",
        "{male_name}-{male_name} {uppercase_letter}. {last_name}",

    ]

    def on_result(self, result_string):
        return result_string


class FullFemaleNameTemplate(Template):
    pattern_list = [
        "{female_name} {last_name}",
        "{female_name} {last_name}",
        "{female_name} {last_name}",
        "{female_name} {last_name}",
        "{female_name} {last_name}",

        "{female_name}-{female_name} {last_name}",
        "{female_name}-{female_name} {uppercase_letter}. {last_name}",

    ]

    def on_result(self, result_string):
        return result_string


class MaleNameTemplate(Template):
    pattern_list = [
        "{male_name}"
    ]

    def on_result(self, result_string):
        return result_string


class FemaleNameTemplate(Template):
    pattern_list = [
        "{male_name} {last_name}",
        "{male_name} {last_name}",
        "{male_name} {last_name}",
        "{male_name} {last_name}",
        "{male_name} {last_name}",

        "{male_name}-{male_name} {last_name}",
        "{male_name}-{male_name} {uppercase_letter}. {last_name}",
    ]

    def on_result(self, result_string):
        return result_string


class FullNameTemplate(Template):
    pattern_list = FullMaleNameTemplate.pattern_list + FullFemaleNameTemplate.pattern_list

    def on_result(self, result_string):
        return result_string


if __name__ == '__main__':
    import random

    print(FullNameTemplate().render())
