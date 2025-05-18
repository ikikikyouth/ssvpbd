import pandas as pd
import unicodedata
import re

categories = {
    "stepsister_category": ["step sis", "step sister", "step sisters", "step-sis", "step-sister", "step-sisters", "stepsis", "stepsister", "stepsisters", "stepsisses", "stepsisterly"],
    "stepbrother_category": ["step bro", "step brother", "step brothers", "step-brother", "stepbro", "stepbrother", "stepbrothers", "step bros", "step brotherly", "step-bro", "step-bros", "step-brothers", "stepbros", "stepbrotherly"],
    "stepfather_category": ["step dad", "step daddy", "step father", "step-dad", "step-daddy", "stepdad", "stepdaddy", "stepfather", "step daddies", "step daddys", "step fathers", "step dads", "step-daddys", "step-dilf", "step-daddies", "step-dads", "step-father", "step-fathers", "step-pop", "stepdilf", "stepdaddies", "stepdads", "stepdaddys", "stepfathers"],
    "stepmother_category": ["step mom", "step mommy", "step mother", "step-mom", "step-mommy", "step-mother", "stepmama", "stepmom", "stepmommy", "stepmoms", "stepmother", "stepmum", "step milf", "step milfs", "step ma", "step mamacita", "step mommas", "step mommies", "step mommys", "step moms", "step mothers", "step mum", "step-milf", "step-milfs", "step-moms", "step-mothers", "step-mummy", "stepmilf", "stepma", "stepmomma", "stepmommys", "stepmummy", "stepmothers", "stepmums", "stepmummies", "stepmoma", "stepmommies"],
    "stepsiblings_category": ["step siblings", "step-siblings", "stepsiblings", "stepsibs", "step sibling", "step-sibling", "step-sib", "step-sibs", "stepsibling"],
    "stepfamily_category": ["step family", "step-family", "stepfam", "stepfamily", "step familia", "step fam", "step families", "stepfamilies"],
    "stepson_category": ["step son", "step-son", "stepsons", "stepson", "step-sons"],
    "stepdaughter_category": ["step daughter", "step daughters", "stepdaughter", "step-daughter", "stepdaughters", "step-daughters", "step-daddysgirl"],
    "stepcousin_category": ["step-cousin", "stepcousing", "step cousin", "step cousins", "step-cousins", "step-cоusin", "stepcousin", "stepcousins"],
    "undefined_other_step_category": ["step teen", "step relatives", "step-lesbians", "steplesbians", "stepbabe", "stepbae", "stepteen", "stepteens", "step-couple", "stepgodfather"],
    "stepniece_category": ["step niece", "step nieces", "step-niece", "stepniece", "stepnieces"],
    "stepnephew_category": ["step-nephew", "step nephew", "stepnephew", "step nephews", "stepnephews"],
    "stepaunt_category": ["step aunt", "step aunts", "stepaunt", "stepauntie", "step auntie", "step aunty", "step-aunt", "step-auntie", "step-aunty", "step-aunts", "stepaunts", "stepaunty"],
    "stepuncle_category": ["step uncle", "step uncles", "stepuncle", "stepuncles", "step-uncles"],
    "stepgrandmother_category": ["stepgrandma", "step grandma", "step grandmas", "step grandmom", "step grandmother", "step granny", "step nana", "step-grandma", "step-granny", "step-nana", "stepgrandmom", "stepgranny", "stepnana", "stepgrams", "stepgrandmother", "stepnanas", "step grannies", "step-grandmother", "stepgrandmas"],
    "stepgrandfather_category": ["stepgrandpa", "step grandad", "step grandfather", "step grandpa", "step-grandfather", "step-grandpa", "stepgrandpas"],
    "stepgranddaughter_category": ["step granddaughter", "step-granddaughter", "stepgranddaughter", "step grandaughter"],
    "stepgrandson_category": ["step grandson", "step grandsons", "step-grandson", "stepgrandson", "stepgrandsons", "step grand son"]
}

df = pd.read_excel("20152024overall_cleaned.xlsx")
df.columns = df.columns.str.strip() 

df["Title"] = df["Title"].astype(str).str.lower().str.strip()
df["Title"] = df["Title"].apply(lambda x: unicodedata.normalize('NFKD', x))

for category, keywords in categories.items():
    pattern = "|".join(re.escape(kw) for kw in keywords)
    filtered_df = df[df["Title"].str.contains(pattern, case=False, na=False, regex=True)]
    
    if not filtered_df.empty:
        output_file = f"{category}.xlsx"
        filtered_df.to_excel(output_file, index=False)
        print(f"done: {output_file}")
    else:
        print(f"nepavyko")

print("done")
