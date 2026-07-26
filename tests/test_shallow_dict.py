import unittest

from utils_future import ShallowDict

TEST_DATA = {
    "Person": {
        "Time:2024": {
            "AgeGroup:3To4Years": {
                "EducationActivity:preschool_education": {
                    "Count": "Int:239687"
                },
                "EducationActivity:school_education": {"Count": "Int:0"},
                "EducationActivity:degree_or_postgraduate_education": {
                    "Count": "Int:0"
                },
                "EducationActivity:vocational_training_or_technical_education": {
                    "Count": "Int:0"
                },
                "EducationActivity:other_educational_activity": {
                    "Count": "Int:568"
                },
                "EducationActivity:not_studying": {"Count": "Int:327724"},
            },
            "AgeGroup:5To14Years": {
                "EducationActivity:preschool_education": {
                    "Count": "Int:243587"
                },
                "EducationActivity:school_education": {
                    "Count": "Int:2909880"
                },
                "EducationActivity:degree_or_postgraduate_education": {
                    "Count": "Int:0"
                },
                "EducationActivity:vocational_training_or_technical_education": {
                    "Count": "Int:0"
                },
                "EducationActivity:other_educational_activity": {
                    "Count": "Int:23042"
                },
                "EducationActivity:not_studying": {"Count": "Int:115210"},
            },
            "AgeGroup:15To18Years": {
                "EducationActivity:preschool_education": {"Count": "Int:0"},
                "EducationActivity:school_education": {
                    "Count": "Int:1148649"
                },
                "EducationActivity:degree_or_postgraduate_education": {
                    "Count": "Int:4340"
                },
                "EducationActivity:vocational_training_or_technical_education": {
                    "Count": "Int:14467"
                },
                "EducationActivity:other_educational_activity": {
                    "Count": "Int:33273"
                },
                "EducationActivity:not_studying": {"Count": "Int:245932"},
            },
            "AgeGroup:19To24Years": {
                "EducationActivity:preschool_education": {"Count": "Int:0"},
                "EducationActivity:school_education": {"Count": "Int:295504"},
                "EducationActivity:degree_or_postgraduate_education": {
                    "Count": "Int:213311"
                },
                "EducationActivity:vocational_training_or_technical_education": {
                    "Count": "Int:82193"
                },
                "EducationActivity:other_educational_activity": {
                    "Count": "Int:115462"
                },
                "EducationActivity:not_studying": {"Count": "Int:1250512"},
            },
            "AgeGroup:25To125Years": {
                "EducationActivity:preschool_education": {"Count": "Int:0"},
                "EducationActivity:school_education": {"Count": "Int:0"},
                "EducationActivity:degree_or_postgraduate_education": {
                    "Count": "Int:110971"
                },
                "EducationActivity:vocational_training_or_technical_education": {
                    "Count": "Int:27743"
                },
                "EducationActivity:other_educational_activity": {
                    "Count": "Int:97099"
                },
                "EducationActivity:not_studying": {"Count": "Int:13635505"},
            },
        }
    }
}

TEST_DATA_SHALLOW = {
    (
        'Person',
        'Time:2024',
        'AgeGroup:3To4Years',
        'EducationActivity:preschool_education',
        'Count',
    ): 'Int:239687',
    (
        'Person',
        'Time:2024',
        'AgeGroup:3To4Years',
        'EducationActivity:school_education',
        'Count',
    ): 'Int:0',
    (
        'Person',
        'Time:2024',
        'AgeGroup:3To4Years',
        'EducationActivity:degree_or_postgraduate_education',
        'Count',
    ): 'Int:0',
    (
        'Person',
        'Time:2024',
        'AgeGroup:3To4Years',
        'EducationActivity:vocational_training_or_technical_education',
        'Count',
    ): 'Int:0',
    (
        'Person',
        'Time:2024',
        'AgeGroup:3To4Years',
        'EducationActivity:other_educational_activity',
        'Count',
    ): 'Int:568',
    (
        'Person',
        'Time:2024',
        'AgeGroup:3To4Years',
        'EducationActivity:not_studying',
        'Count',
    ): 'Int:327724',
    (
        'Person',
        'Time:2024',
        'AgeGroup:5To14Years',
        'EducationActivity:preschool_education',
        'Count',
    ): 'Int:243587',
    (
        'Person',
        'Time:2024',
        'AgeGroup:5To14Years',
        'EducationActivity:school_education',
        'Count',
    ): 'Int:2909880',
    (
        'Person',
        'Time:2024',
        'AgeGroup:5To14Years',
        'EducationActivity:degree_or_postgraduate_education',
        'Count',
    ): 'Int:0',
    (
        'Person',
        'Time:2024',
        'AgeGroup:5To14Years',
        'EducationActivity:vocational_training_or_technical_education',
        'Count',
    ): 'Int:0',
    (
        'Person',
        'Time:2024',
        'AgeGroup:5To14Years',
        'EducationActivity:other_educational_activity',
        'Count',
    ): 'Int:23042',
    (
        'Person',
        'Time:2024',
        'AgeGroup:5To14Years',
        'EducationActivity:not_studying',
        'Count',
    ): 'Int:115210',
    (
        'Person',
        'Time:2024',
        'AgeGroup:15To18Years',
        'EducationActivity:preschool_education',
        'Count',
    ): 'Int:0',
    (
        'Person',
        'Time:2024',
        'AgeGroup:15To18Years',
        'EducationActivity:school_education',
        'Count',
    ): 'Int:1148649',
    (
        'Person',
        'Time:2024',
        'AgeGroup:15To18Years',
        'EducationActivity:degree_or_postgraduate_education',
        'Count',
    ): 'Int:4340',
    (
        'Person',
        'Time:2024',
        'AgeGroup:15To18Years',
        'EducationActivity:vocational_training_or_technical_education',
        'Count',
    ): 'Int:14467',
    (
        'Person',
        'Time:2024',
        'AgeGroup:15To18Years',
        'EducationActivity:other_educational_activity',
        'Count',
    ): 'Int:33273',
    (
        'Person',
        'Time:2024',
        'AgeGroup:15To18Years',
        'EducationActivity:not_studying',
        'Count',
    ): 'Int:245932',
    (
        'Person',
        'Time:2024',
        'AgeGroup:19To24Years',
        'EducationActivity:preschool_education',
        'Count',
    ): 'Int:0',
    (
        'Person',
        'Time:2024',
        'AgeGroup:19To24Years',
        'EducationActivity:school_education',
        'Count',
    ): 'Int:295504',
    (
        'Person',
        'Time:2024',
        'AgeGroup:19To24Years',
        'EducationActivity:degree_or_postgraduate_education',
        'Count',
    ): 'Int:213311',
    (
        'Person',
        'Time:2024',
        'AgeGroup:19To24Years',
        'EducationActivity:vocational_training_or_technical_education',
        'Count',
    ): 'Int:82193',
    (
        'Person',
        'Time:2024',
        'AgeGroup:19To24Years',
        'EducationActivity:other_educational_activity',
        'Count',
    ): 'Int:115462',
    (
        'Person',
        'Time:2024',
        'AgeGroup:19To24Years',
        'EducationActivity:not_studying',
        'Count',
    ): 'Int:1250512',
    (
        'Person',
        'Time:2024',
        'AgeGroup:25To125Years',
        'EducationActivity:preschool_education',
        'Count',
    ): 'Int:0',
    (
        'Person',
        'Time:2024',
        'AgeGroup:25To125Years',
        'EducationActivity:school_education',
        'Count',
    ): 'Int:0',
    (
        'Person',
        'Time:2024',
        'AgeGroup:25To125Years',
        'EducationActivity:degree_or_postgraduate_education',
        'Count',
    ): 'Int:110971',
    (
        'Person',
        'Time:2024',
        'AgeGroup:25To125Years',
        'EducationActivity:vocational_training_or_technical_education',
        'Count',
    ): 'Int:27743',
    (
        'Person',
        'Time:2024',
        'AgeGroup:25To125Years',
        'EducationActivity:other_educational_activity',
        'Count',
    ): 'Int:97099',
    (
        'Person',
        'Time:2024',
        'AgeGroup:25To125Years',
        'EducationActivity:not_studying',
        'Count',
    ): 'Int:13635505',
}


class TestCase(unittest.TestCase):
    def test_method(self):
        shallow_d = ShallowDict.from_deep(TEST_DATA)
        self.assertEqual(shallow_d.get_dict(), TEST_DATA_SHALLOW)
        deep_d = shallow_d.to_deep()
        self.assertEqual(TEST_DATA, deep_d)
        self.assertLessEqual(len(str(deep_d)), len(str(shallow_d.get_dict())))
