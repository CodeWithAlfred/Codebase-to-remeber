class Pupils {
    constructor(
        name,age,grade,hometown
    ){
        this.name = name;
        this.age = age
        this.grade = grade
        this.hometown = hometown
    }

    setter(name, age, grade, hometown){
        this.name = name;
        this.age= age;
        this.grade = grade;
        this.hometown = hometown
    }

    getter(){
        console.table(this.name, this.age, this.grade, this.hometown)
    }
}


const p1 = new Pupils('Alfred', 24, 93, "Nairobi");

p1.getter()