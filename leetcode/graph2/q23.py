from collections import defaultdict
import heapq

positive_feedback = ["fkeofjpc","qq","iio"]
negative_feedback = ["jdh","khj","eget","rjstbhe","yzyoatfyx","wlinrrgcm"]
report=["rjstbhe eget kctxcoub urrmkhlmi yniqafy fkeofjpc iio yzyoatfyx khj iio","gpnhgabl qq qq fkeofjpc dflidshdb qq iio khj qq yzyoatfyx","tizpzhlbyb eget z rjstbhe iio jdh jdh iptxh qq rjstbhe","jtlghe wlinrrgcm jnkdbd k iio et rjstbhe iio qq jdh","yp fkeofjpc lkhypcebox rjstbhe ewwykishv egzhne jdh y qq qq","fu ql iio fkeofjpc jdh luspuy yzyoatfyx li qq v","wlinrrgcm iio qq omnc sgkt tzgev iio iio qq qq","d vhg qlj khj wlinrrgcm qq f jp zsmhkjokmb rjstbhe"]

student_id = [96537918,589204657,765963609,613766496,43871615,189209587,239084671,908938263]

k = 3

pos_dic=defaultdict(int)
neg_dic=defaultdict(int)

for w in positive_feedback:
    pos_dic[w]=3

for w in negative_feedback:
    neg_dic[w]=-1

ans=[]

for i in range(len(report)):
    curSum=0
    for w in report[i].split(" "):
        if w=="no":
            continue
        if w in pos_dic:
            curSum+=pos_dic[w]
            continue
        if w in neg_dic:
            curSum+=neg_dic[w]
    
    ans.append([curSum,student_id[i]])
  
sorted_data = sorted(ans, key=lambda x: (-x[0], x[1]))
res=[a[1] for a in sorted_data]
print(sorted_data)



