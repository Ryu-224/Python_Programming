import os
import pickle

filepath = 'data/score.bin'

def input_scores():
    s = []
    i = 1
    print("[점수 입력]")

    while True:
        n = int(input(f"#{i}? "))
        if n < 0:
            break
        s.append(n)
        i += 1
    
    return s

def get_average(s):
    total = 0
    for n in s:
        total += n
    a = total / len(s)
    return a

def show_scores(s):
    print("\n[점수 출력]")
    print("개인 점수: ", end = "")
    for n in s:
        print(n, end = " ")
    print()

def save_scores(s, a):
    with open(filepath, 'wb') as file:
        pickle.dump((s, a), file)

def load_scores():
    with open(filepath, 'rb') as file:
        s, a = pickle.load(file)
        return s, a
    
if not(os.path.isdir('data')):
    os.makedirs('data')

if os.path.exists(filepath):
    print('[파일 읽기]')
    scores, avg = load_scores()
    show_scores(scores)
    print(f"평균: {avg:.1f}")

else:
    scores = input_scores()
    avg = get_average(scores)
    show_scores(scores)
    print(f"평균: {avg:.1f}")
    save_scores(scores, avg)