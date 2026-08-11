def calculate_average(scores):
    if not scores:
        return 0
    else:
        sum=0
        for score in scores:
            sum+=score
        return round(sum/len(scores),1)

print(calculate_average([80, 81, 82]))

def find_max_score(scores):
    if not scores:
        return None
    maxscore=0
    for score in scores:
        if score>maxscore:
            maxscore=score
    return maxscore

print(find_max_score([80, 81, 82]))

def count_passed_students(scores, pass_score=60):
    if not scores:
            return 0
    len=0
    for score in scores:
        if score<pass_score:
            len+=1
    return len

scores = [55, 61, 90, 60]
print(count_passed_students(scores))

def generate_report(name, scores):
    dic=dict()
    dic['name']=name
    dic['average']=calculate_average(scores)
    dic['max_score']=find_max_score(scores)
    dic['passed_count']=count_passed_students(scores)
    return dic

print(generate_report('熊二',[55, 61, 90, 60]))
