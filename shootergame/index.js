
// Selecting Canvas element
const canvas = document.querySelector('canvas')

// Adjusting Canvas dimensions to our window
canvas.width = innerWidth
canvas.height = innerHeight

// Accessing the Canvas properties
const c = canvas.getContext('2d')

// Creating a Class for the Player

class Player{
    // Parameters of the character 
    constructor(x,y,radius,color){
        this.x = x
        this.y = y
        this.radius = radius
        this.color = color    
    }

    // Creating a function that draws the character
    draw(){
        c.beginPath()
        c.arc(this.x,this.y,this.radius,0,Math.PI*2,false)
        c.fillStyle = this.color
        c.fill()
    }
}

// Creating a Class for the Projectile

class Projectile{
    constructor(x,y,radius,color,velocity){
        this.x = x
        this.y = y
        this.radius = radius
        this.color = color 
        this.velocity = velocity
    }
    draw(){
        c.beginPath()
        c.arc(this.x,this.y,this.radius,0,Math.PI*2,false)
        c.fillStyle = this.color
        c.fill()
    }

    update(){
        this.x = this.x + this.velocity.x
        this.y = this.y + this.velocity.y
    }
}

// Creating an Enermy class
class Enemy{
    constructor(x,y,radius,color,velocity){
        this.x = x
        this.y = y
        this.radius = radius
        this.color = color 
        this.velocity = velocity
    }
    draw(){
        console.log("enemy is being drawn!!")
        c.beginPath()
        c.arc(this.x,this.y,this.radius,0,Math.PI*2,false)
        c.fillStyle = this.color
        c.fill()
    }

    update(){
        this.x = this.x + this.velocity.x
        this.y = this.y + this.velocity.y
    }
}

// Creating  Projectiles and Enemies array

const projectiles = []
const Enemies = []

// function to spawn enemeies

function spawnEnemies(){
    setInterval(()=> {
        var x = 0
        var y = 0

        // choosing a random position to spawn the enemy
        const choice = Math.round(Math.random()*100)
        if (choice >0 && choice <= 20){
            x = canvas.width*Math.random()
            y = 0
        }
        else if ( choice > 20 && choice <=40){
            x = canvas.width*Math.random()
            y = canvas.height
        }
        else if (choice >=40 && choice <=60){
            y = canvas.height*Math.random()
            x = 0
        }
        else{
            x = canvas.width
            y = canvas.height*Math.random()
            
        }
        
        //Selecting a random radius
        r = Math.random()
        if (r<0.5){
            r = r*5
        }
        const radius = r*40
        
        
        console.log(choice)
        // Calculating the angle at which it
        // should move to reach the player
        const angle = Math.atan2(
            canvas.height/2-y,
            canvas.height/2-x
        )

        // Pushing enemy into the stack
        Enemies.push(
        new Enemy(x,
                  y,
                  radius,
                  'black',
                  {
                    x: 5*Math.cos(angle),
                    y: 5*Math.sin(angle)
                } 
            )
        )
    },2000)
}

// Function that runs the animations
let animationId
function animate(){
    animationId = requestAnimationFrame(animate)
    console.log(Enemies)
    console.log(projectiles)
    
    // Clears the window
    c.clearRect(0,0,canvas.width, canvas.height)
    
    // Redrawing our character
    player.draw()

    // Iterates through the projectiles to shoot
    projectiles.forEach((projectile,index3) => {
        projectile.update()
        projectile.draw()

    })

    // Iterating through each Enemy
    Enemies.forEach((enemy, index) => {
        enemy.update()
        enemy.draw()

        

        // Checking if the projectile has touched the enemy

        projectiles.forEach((projectile, index2)=>{
            const dist = Math.sqrt((projectile.x-enemy.x)**2 + (projectile.y - enemy.y)**2)
            if ( dist < enemy.radius){
                setTimeout(() =>{
                    Enemies.splice(index,1)
                    projectiles.splice(index2,1)
                })
                
            }
        })

        const dist2 = Math.sqrt((player.x-enemy.x)**2 + (player.y - enemy.y)**2)
            if (dist2 < player.radius){
                cancelAnimationFrame(animationId)
            }
    })

}


// Drawing out the Main character 
const player = new Player(canvas.width/2,canvas.height/2,30,'blue') 
player.draw()


// Event Listeners
 addEventListener('click',(event) => {
    const angle = Math.atan2(
        event.clientY - canvas.height / 2,
        event.clientX - canvas.width / 2
    )
    projectiles.push(
        new Projectile(
            canvas.width/2,
            canvas.height/2,
            5,
            'red',
            {
                x: 10*Math.cos(angle),
                y: 10*Math.sin(angle)
            }            
        )
    )
 })

animate()
spawnEnemies()