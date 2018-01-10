remove_elemento([Ch|R], Ch, R).
remove_elemento([I|R], Ch, [I|RR]):- remove_elemento(R, Ch, RR).

insere_inicio(L, Ch, [Ch|L]).

insere_final([ ], Ch, [Ch]).
insere_final([I|R], Ch, [I|RR]):- insere_final(R, Ch, RR).

insere_inicio_final(_, [ ], [ ]).
insere_inicio_final(Ch, [I|R], [III|RR]):- insere_inicio(I, Ch, II), insere_final(II, Ch, III), insere_inicio_final(Ch, R, RR).

acha_arco(_, _, [ ], 999999).
acha_arco(I, F, [arco(I, F, Ch) | _], Ch).
acha_arco(I, F, [_|R], Ch):- acha_arco(I, F, R, Ch).

cacheiro(L, Arcos, [Ac|L]):- cacheiro1(L, Arcos, 0, Ac).
cacheiro1([ ], _, Ac, Ac).
cacheiro1([_|R], _, Ac, Acc):- R = [ ], Acc = Ac.
cacheiro1([I|[F|R]], Arcos, Ac, Accc):- acha_arco(I, F, Arcos, Ch), Acc is Ac + Ch, cacheiro1([F|R], Arcos, Acc, Accc).

cacheiros([ ], _, [ ]).
cacheiros([F|R], Arcos, [FF|RR]):- cacheiro(F, Arcos, FF), cacheiros(R, Arcos, RR).

imprimir([[F|R]|_]):- F>=999999->print("NADA"),nl;(print(F),nl,print(R)),nl.

main:- read(Cidades), read(Arcos), read(Cidade_inicial), remove_elemento(Cidades, Cidade_inicial, Aux), findall(P, permutation(Aux, P), Permutacao), insere_inicio_final(Cidade_inicial, Permutacao, Caminhos),cacheiros(Caminhos, Arcos, Tamanho_Caminhos), sort(Tamanho_Caminhos, Ordenada), imprimir(Ordenada).
