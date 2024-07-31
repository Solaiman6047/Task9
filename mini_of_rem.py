def min_removals_to_equal_frequency(s: str) -> int:
    for i in s:
        if i not in count:
            count.update({i:1})
        else:
            count[i]+=1
    mini = min(count.values())
    mini_removal=len(s) - (mini * len(count))
    return mini_removal
 
 

s=list(input("Enter letters: "))
count={
    
}
print(min_removals_to_equal_frequency(s))