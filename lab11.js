<script>
var age=window.prompt("What's your age? ");
var name=window.prompt("What's your name? ");
const ratings=['G', 'PG', 'PG-13', 'R', 'NC-17'];
function movieFunction(age){
  if (age >= 18)
    return (ratings[4])
  else if (age >= 17)
    return (ratings[3])
  else if (age >= 13)
    return (ratings[2])
  else if (age < 13)
    return (ratings[1])
}
console.log("Welcome " + name + ", you may watch movies rated up to " + movieFunction(age))
</script)