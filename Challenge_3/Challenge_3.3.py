def solution(l):
# Reference: https://codereview.stackexchange.com/questions/144510/google-foobar-challenge-lucky-triples
    output=0
    i_start=1
    i_end=len(l)-1
    for idx, i in enumerate(l[i_start:i_end]):
        divisor=multiply=0

        for d in l[:idx+i_start]:
            if i%d==0:
                divisor+=1
        for m in l[idx+i_start+1:]:
            if m%i==0:
                multiply+=1

        output+=divisor*multiply 
    
    return output
