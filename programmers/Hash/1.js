function solution(participant, completion) {
    var answer = '';
    const table={};
    participant.forEach((el)=>{
        if (table[el]===undefined){
            table[el]=1;
        }
        else{
            table[el]+=1;
        }
    });
    completion.forEach((el)=>{
       if(table[el]===undefined){
           answer=el;
           return
       } 
        table[el]-=1;
        if(table[el]===0){
            delete table[el];
        }
    });
    answer=Object.keys(table)[0];
    return answer;
}

//https://programmers.co.kr/learn/courses/30/lessons/42576
