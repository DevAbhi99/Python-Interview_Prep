class Solution:
  def compare(self, str1, str2):
    # TODO: Write your code here
    l1=list(str1)
    l2=list(str2)
    st1=[]
    st2=[]
    pattern='abcdefghijklmnopqrstuvwxyz'


    #Approach used is stack approach

    #New Computation


    if len(str1)==1 and len(str2)==1:
      if (str1[0]=='#' and str2[0]=='#') or (str1[0]==str2[0]):
        return True


    #computation for str1
    while l1:
      popped=l1.pop()
      if st1 and st1[len(st1)-1]=='#' and popped.lower() in pattern:
        st1.pop()
      else:
        st1.append(popped)

    #computation for str2
    while l2:
      popped=l2.pop()
      if st2 and st2[len(st2)-1]=='#' and popped.lower() in pattern:
        st2.pop()
      else:
        st2.append(popped)
    
    st1.reverse()

    st2.reverse()

    return ''.join(st1).replace('#', '')==''.join(st2).replace('#', '')    
