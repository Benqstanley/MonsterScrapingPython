import urllib
import urllib.request
import requests
import lxml
import pandas
from bs4 import BeautifulSoup, NavigableString, Tag

def ReturnTraits(tag):
    return tag.name == 'h2' and tag.text == "Traits"
def ReturnActions(tag):
    return tag.name == 'h2' and tag.text == 'Actions'
def ReturnLegendaryActions(tag):
    return tag.name == 'h2' and tag.text == "Legendary Actions"


def MonsterNames(tag):
    return 'li' in tag and "a href" not in tag
def MonsterSenses(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Senses"
def MonsterImmunities(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Immunities"
def MonsterSkills(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Skills"
def MonsterSavingThrows(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Saving Throws"
def Monster_Size(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Size"
def Monster_Type(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Type"
def Monster_Alignment(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Alignment"
def Monster_AC(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "AC"
def Monster_STR(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "STR"
def Monster_DEX(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "DEX"
def Monster_CON(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "CON"
def Monster_INT(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "INT"
def Monster_WIS(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "WIS"
def Monster_CHA(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "CHA"

def Monster_Speed(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Speed"


def Monster_HP(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "HP"


def Monster_Passive_Perception(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Passive Perception"

def Monster_Languages(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Languages"

def Monster_Vulnerabilities(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Vulnerabilities"

def Monster_Resistances(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Resistances"

def Monster_CR(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Challenge Rating"


def Monster_First_Attack(tag):
    return tag.has_attr("class") and tag.has_attr("data-attribkey") and tag.get('data-attribkey') == "Roll 0"


MonsterListPage = requests.get("https://roll20.net/compendium/dnd5e/Monsters%20by%20Challenge%20Rating#content", auth=('[username]', '[password]'), verify=False)

MonsterList = MonsterListPage.text
soup = BeautifulSoup(MonsterList, "lxml")
list = soup.find_all('a')
MonsterArray = []

for link in list:
    if link.has_attr("href"):
        if "/compendium/dnd5e/Monsters" in link.get('href'):
            MonsterArray.append("https://roll20.net" + link.get('href'))
reorderedAttributes = ['CR', 'Name', 'HP', 'AC', 'Saving Throws', 'Senses', 'Passive Perception', 'Resistances', 'Immunities', 'Vulnerabilities', 'Size', 'Type', 'Alignment', 'STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA', 'Speed', 'Skills']
MonsterDictList = []
MonsterTraitList = []
MonsterActionList = []
MonsterLegendaryActionList = []
monsterNum = 0
#while monsterNum <= 1:
for link in MonsterArray:
    print("Working on Monster " + str(monsterNum))
    MonsterEntry = {}
    MonsterTraitEntry = {}
    MonsterActionEntry = {}
    MonsterLegendaryEntry = {}
    MonsterPageInit = requests.get(MonsterArray[monsterNum], auth=('[username]', '[password]'), verify=False)
    monsterNum = monsterNum + 1
    MonsterPage = MonsterPageInit.text
    MonsterSoup = BeautifulSoup(MonsterPage, "lxml")
    MonsterEntry["Name"] = MonsterSoup.find('h1', {'class', 'page-title'}).text
    MonsterTraitEntry["Name"] = MonsterEntry["Name"]
    MonsterData = MonsterSoup.find("table", {"class", "table table-striped attribtable"})
    MonsterEntry["Size"] = MonsterData.find_all(Monster_Size)[0].find("td").text
    MonsterEntry["Type"] = MonsterData.find(Monster_Type).find("td").text
    MonsterEntry["Alignment"] = MonsterData.find(Monster_Alignment).find("td").text
    MonsterEntry["STR"] = MonsterData.find(Monster_STR).find("td").text
    MonsterEntry["DEX"] = MonsterData.find(Monster_DEX).find("td").text
    MonsterEntry["CON"] = MonsterData.find(Monster_CON).find("td").text
    MonsterEntry["INT"] = MonsterData.find(Monster_INT).find("td").text
    MonsterEntry["WIS"] = MonsterData.find(Monster_WIS).find("td").text
    MonsterEntry["CHA"] = MonsterData.find(Monster_CHA).find("td").text
    MonsterEntry["Speed"] = MonsterData.find(Monster_Speed).find("td").text.replace(" ft.", "")
    MonsterEntry["HP"] = MonsterData.find(Monster_HP).find("td").text
    MonsterEntry["AC"] = MonsterData.find(Monster_AC).find("td").text
    MonsterEntry["Passive Perception"] = MonsterData.find(Monster_Passive_Perception).find("td").text
    if not MonsterData.find(Monster_Languages)is None:
        MonsterEntry["Languages"] = MonsterData.find(Monster_Languages).find("td").text
    if not MonsterData.find(Monster_Vulnerabilities) is None:
        MonsterEntry["Vulnerabilities"] = MonsterData.find(Monster_Vulnerabilities).find("td").text
    if not MonsterData.find(Monster_Resistances) is None:
        MonsterEntry["Resistances"] = MonsterData.find(Monster_Resistances).find("td").text
    if not MonsterData.find(Monster_CR) is None:
        MonsterEntry["CR"] = MonsterData.find(Monster_CR).find("td").text
    if not MonsterData.find(Monster_First_Attack) is None:
        MonsterEntry["First Attack"] = MonsterData.find(Monster_First_Attack).find("td").text
    if not MonsterData.find(MonsterSavingThrows) is None:
        MonsterEntry["Saving Throws"] = MonsterData.find(MonsterSavingThrows).find("td").text
    if not MonsterData.find(MonsterSenses) is None:
        MonsterEntry["Senses"] = MonsterData.find(MonsterSenses).find("td").text
    if not MonsterData.find(MonsterImmunities) is None:
        MonsterEntry["Immunities"] = MonsterData.find(MonsterImmunities).find("td").text
    if not MonsterData.find(MonsterSkills) is None:
        MonsterEntry["Skills"] = MonsterData.find(MonsterSkills).find("td").text
    Cat = MonsterSoup.find("div", {'class', 'pagecontent'}).find(ReturnTraits)
    if Cat is not None:
        traitNum = 0
        entryID = ""
        for item in Cat.next_siblings:
            if item.name == 'h2' and item.text == "Actions":
                break
            elif item.name == 'strong':
                traitNum = traitNum + 1
                trait = item.text
                for sib in item.next_siblings:
                    if isinstance(sib, NavigableString):
                        trait = trait + sib
                    elif isinstance(sib, Tag) and sib.name != 'br':
                        trait = trait + sib.text
                    else:
                        break
                entryID = "Trait" + str(traitNum)
                MonsterTraitEntry[entryID] = trait
    MonsterTraitList.append(MonsterTraitEntry)
    Cat = MonsterSoup.find("div", {'class', 'pagecontent'}).find(ReturnActions)
    if Cat is not None:
        MonsterActionEntry["Name"] = MonsterEntry["Name"]
        traitNum = 0
        entryID = ""
        for item in Cat.next_siblings:
            if item.name == 'h2' and item.text == "Legendary Actions":
                MonsterLegendaryEntry["Info"] = item.next_sibling
            elif item.name == 'strong':
                traitNum = traitNum + 1
                action = item.text
                for sib in item.next_siblings:
                    if isinstance(sib, NavigableString):
                        action = action + sib
                    elif isinstance(sib, Tag) and sib.name != 'br':
                        action = action + sib.text
                    else:
                        break
                entryID = "Action" + str(traitNum)
                MonsterActionEntry[entryID] = action
    MonsterActionList.append(MonsterActionEntry)
    Cat = MonsterSoup.find("div", {'class', 'pagecontent'}).find(ReturnLegendaryActions)
    if not Cat is None:
        MonsterLegendaryEntry["Name"] = MonsterEntry["Name"]
        entryID = ""
        traitNum = 0
        for item in Cat.next_siblings:
            if item.name == 'h2' and item.text != "Legendary Actions":
                break
            elif item.name == 'strong':
                traitNum = traitNum + 1
                Laction = item.text
                for sib in item.next_siblings:
                    if isinstance(sib, NavigableString):
                        Laction = Laction + sib
                    elif isinstance(sib, Tag) and sib.name != 'br':
                        Laction = Laction + sib.text
                    else:
                        break
                entryID = "Legendary Action" + str(traitNum)
                MonsterLegendaryEntry[entryID] = Laction
    MonsterLegendaryActionList.append(MonsterLegendaryEntry)
    MonsterDictList.append(MonsterEntry)
reorderedTraits = ['Name','Trait1', 'Trait2', 'Trait3', 'Trait4', 'Trait5', 'Trait6', 'Trait7']
reorderedActions = ['Name','Action1', 'Action2', 'Action3', 'Action4', 'Action5', 'Action6']
MonsterDF = pandas.DataFrame(MonsterDictList, columns=reorderedAttributes)
MonsterTraitDF = pandas.DataFrame(MonsterTraitList, columns=reorderedTraits)
MonsterActionDF = pandas.DataFrame(MonsterActionList, columns=reorderedActions)
MonsterLegendaryDF = pandas.DataFrame(MonsterLegendaryActionList)
MonsterDF.to_csv("MonsterList.csv")
MonsterTraitDF.to_csv("MonsterTraitList.csv")
MonsterActionDF.to_csv("MonsterActionList.csv")
MonsterLegendaryDF.to_csv("MonsterLegendaryActionList.csv")
