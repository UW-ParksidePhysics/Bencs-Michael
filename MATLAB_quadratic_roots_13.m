%Code Written by Julia Jones and Michael Bencs

a= input('Enter the coefficient a: ')
b= input('Enter the coefficient b: ')
c= input('Enter the coefficient c: ')


discr = b*b - 4*a*c;
d= sqrt(discr)
if discr < 0
disp('Warning: discriminant is negative, roots are imaginary');
d=sqrt(d^2)
x1_imaginary= (-b-d)/(2*a)
x2_imaginary= (-b+d)/(2*a)

elseif discr == 0

disp('Discriminant is zero, roots are repeated')
xZero= -b/(2*a)
else
disp('Roots are real')

x1= (-b-d)/(2*a)
x2= (-b+d)/(2*a)
end
