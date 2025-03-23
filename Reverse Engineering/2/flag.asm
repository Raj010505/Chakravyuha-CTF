section .text
    global encrypt_flag

encrypt_flag:
    mov rsi, rdi       
    mov rdi, rsi       
    xor rcx, rcx        

encrypt_loop:
    movzx rax, byte [rsi + rcx]  
    test  al, al                 
    jz   encryption_done         

    shl  rax, 8                  

    inc  rcx                     
    movzx rbx, byte [rsi + rcx]  
    test  bl, bl                 
    jz    zero_pad               

    or   rax, rbx                
    jmp  store_char

zero_pad:
    or   rax, 0                  

store_char:
    mov [rdi], rax               
    add rdi, 2                   
    inc rcx                      
    jmp encrypt_loop             

encryption_done:
    ret
