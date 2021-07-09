from categories import Category
import bayes

dict1 = {
    Category.NEW_RELEASES: {'dear': 0.47, 'friend':0.29, 'lunch': 0.18, 'money':0.06},
    Category.UPDATES: {'dear': 0.29, 'friend':0.14, 'money':0.57},
    Category.RUMOURS: {},
    Category.REVIEWS: {},
    Category.COMMENTARY: {},
    Category.WALKTHROUGHS: {},
    Category.ANNOUNCEMENTS: {}
}

dict2 = {
    Category.NEW_RELEASES: 0.67,
    Category.UPDATES: 1 - 0.67,
    Category.RUMOURS: 0*0.14,
    Category.REVIEWS: 0*0.14,
    Category.COMMENTARY: 0*0.14,
    Category.WALKTHROUGHS: 0*0.14,
    Category.ANNOUNCEMENTS: 0*0.14
}

print(bayes.bayes(["lunch","money","money","money","money"],dict1,dict2,0.1))
