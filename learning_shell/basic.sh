# output a sentence
echo "Hello World!"

# variable
var="this is a variable!"
echo $var

# read from cmd
echo "do you...?(y/n):"
read readAll

# if-else
if [[ $readAll = "y" ]]; then
    echo yes
else
    echo "no"
fi

# declare a array
story_list=(hello0 hello1 hello2)

# for loop
for i in {0..2};
do
    # random access of array
    echo ${story_list[$i]}
done

# change the variable value
var1=123
for i in {0..5};
do
    echo $(($var1+i))
done

# open and write a file
a="Hello world"
FILE="./filename.txt"
echo $a >> $FILE
echo "----------------------" >> $FILE

# read and print a file
echo "reading filename.txt"
cat filename.txt | while read line
do
    echo $line
done

# exacute a program and write the output to a file
cmd=`echo "Hello World"`
a=${cmd}
FILE="./output.txt"
echo "$a" >> $FILE

echo ""
