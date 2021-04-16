# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

mortality_scale = []
for death in deaths:
    if deaths == 0:
        mortality_scale.append(0)
    elif death <= 100:
        mortality_scale.append(1)
    elif death <= 500:
        mortality_scale.append(2)
    elif death <= 1000:
        mortality_scale.append(3)
    elif death <= 10000:
        mortality_scale.append(4)
    else:
        mortality_scale.append(5)

# print(mortality_scale)


# write your update damages function here:

def damages_updates(damages):
    new_list = []
    for damage in damages:
        if damage[-1] == 'M':
            # 1000000
            new_list.append(float(damage.replace('M', '')) * 1000000)
        elif damage[-1] == 'B':
            # 1000000000
            new_list.append(float(damage.replace('B', '')) * 1000000000)
        else:
            new_list.append(damage)
    return new_list


dmg = damages_updates(damages)

# write your construct hurricane dictionary function here:
dict_hurricane = {}
for counter, i in enumerate(names):
    dict_hurricane[i] = {'Name': names[counter],
                         'Month': months[counter],
                         'Year': years[counter],
                         'Max Sustained Wind': max_sustained_winds[counter],
                         'Areas Affected': areas_affected[counter],
                         'Damage': dmg[counter],
                         'Deaths': deaths[counter]
                         }


# print(dict_hurricane['Cuba I'])
# print(dict_hurricane[names[1]])

# write your construct hurricane by year dictionary function here:
def dict_year():
    year_dict = {}
    for counter, name in enumerate(names):
        current_year = years[counter]
        current_cane = dict_hurricane[name]
        if current_year in year_dict.keys():
            year_dict[current_year].append(current_cane)
        else:
            year_dict[current_year] = [current_cane]
    return year_dict


year_categorized = dict_year()

# print(year_categorized[2005])


# write your count affected areas function here:
def future_hurricanes():
    afected_area = {}
    for areas in areas_affected:
        for area in areas:
            if area in afected_area.keys():
                afected_area[area] += 1
            else:
                afected_area[area] = 1
    return afected_area


area_counter = future_hurricanes()


# write your find most affected area function here:
def most_hurricanes():
    list_of_max = []
    max_value = max(area_counter.values())
    for key in area_counter:
        if area_counter[key] == max_value:
            list_of_max.append(key)
    return list_of_max


# print(most_hurricanes())

# write your greatest number of deaths function here:
def step_07():
    max_deaths = 0
    for area in names:
        if dict_hurricane[area]['Deaths'] > max_deaths:
            max_deaths = dict_hurricane[area]['Deaths']
            name_of_hurricane = dict_hurricane[area]['Name']
    return max_deaths, name_of_hurricane


# print(step_07())

# write your catgeorize by mortality function here:
mortality_dict = {}
for ms, name in zip(mortality_scale, names):
    if ms in mortality_dict.keys():
        mortality_dict[ms].append(name)
    else:
        mortality_dict[ms] = [name]

kommas = list(mortality_dict.keys()).sort
print(kommas)
for i in mortality_dict.keys():
    print(i, mortality_dict[i])

# write your greatest damage function here:


# write your catgeorize by damage function here:
