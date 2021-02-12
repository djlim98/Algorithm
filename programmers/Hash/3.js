function solution(clothes) {
    var answer = 0;
    const type={};
    clothes.forEach((el)=>{
       type[el[1]]=(type[el[1]]|0)+1;
    });
    const multi=Object.values(type);
    let temp=1;
    while(multi.length){
       temp*=(multi.pop()+1) 
    }
    temp-=1;
    answer=temp
    return answer;
}

//https://programmers.co.kr/learn/courses/30/lessons/42578
