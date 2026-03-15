       IDENTIFICATION DIVISION.
       PROGRAM-ID. PROCESADOR-BATCH.
       AUTHOR. Ramón Romero Montilla.
       
       ENVIRONMENT DIVISION.
       INPUT-OUTPUT SECTION.
       FILE-CONTROL.
           SELECT MAESTRO-FILE ASSIGN TO 'data/maestro.dat'
               ORGANIZATION IS LINE SEQUENTIAL.
           
           SELECT MOVIMIENTOS-FILE ASSIGN TO 'data/movimientos.dat'
               ORGANIZATION IS LINE SEQUENTIAL.
           
           SELECT REPORTE-FILE ASSIGN TO 'data/reporte.txt'
               ORGANIZATION IS LINE SEQUENTIAL.

       DATA DIVISION.
       FILE SECTION.
       FD MAESTRO-FILE.
       01 MAESTRO-RECORD PIC X(100).

       FD MOVIMIENTOS-FILE.
       01 MOVIMIENTOS-RECORD PIC X(100).

       FD REPORTE-FILE.
       01 REPORTE-RECORD PIC X(100).

       WORKING-STORAGE SECTION.
       01 WS-VARIABLES.
          05 WS-TOTAL-CUENTAS PIC 999 VALUE 0.
          05 WS-EOF-MAESTRO PIC X VALUE 'N'.
          05 WS-EOF-MOVIMIENTOS PIC X VALUE 'N'.
          05 WS-LINEA-SALIDA PIC X(100).
          05 WS-POS PIC 999.
          05 WS-NUM-CUENTA-STR PIC X(10).
          05 WS-NOMBRE-STR PIC X(30).
          05 WS-SALDO-STR PIC X(20).
          05 WS-TIPO-STR PIC X(1).
          05 WS-MONTO-STR PIC X(20).
          05 WS-NUM-CUENTA-NUM PIC 9(10).
          05 WS-SALDO-NUM PIC 9(10)V99.
          05 WS-MONTO-NUM PIC 9(10)V99.
          05 WS-SALDO-DISPLAY PIC Z(9)9.99.
          05 IDX PIC 999.

       01 TABLA-CUENTAS.
          05 CUENTA OCCURS 100 TIMES INDEXED BY IDX-TAB.
             10 NUM-CUENTA PIC 9(10).
             10 NOMBRE-TITULAR PIC X(30).
             10 SALDO-ACTUAL PIC 9(10)V99.

       PROCEDURE DIVISION.
           PERFORM INICIALIZAR.
           PERFORM CARGAR-MAESTRO.
           PERFORM PROCESAR-MOVIMIENTOS.
           PERFORM GENERAR-REPORTE.
           PERFORM FINALIZAR.
           STOP RUN.

       INICIALIZAR.
           OPEN INPUT MAESTRO-FILE.
           OPEN INPUT MOVIMIENTOS-FILE.
           OPEN OUTPUT REPORTE-FILE.

       CARGAR-MAESTRO.
           PERFORM UNTIL WS-EOF-MAESTRO = 'S'
               READ MAESTRO-FILE
                   AT END
                       MOVE 'S' TO WS-EOF-MAESTRO
                   NOT AT END
                       ADD 1 TO WS-TOTAL-CUENTAS
                       MOVE WS-TOTAL-CUENTAS TO IDX
                       
                       MOVE MAESTRO-RECORD(1:10) 
                           TO WS-NUM-CUENTA-STR
                       MOVE MAESTRO-RECORD(11:30) 
                           TO WS-NOMBRE-STR
                       MOVE MAESTRO-RECORD(41:20) 
                           TO WS-SALDO-STR
                       
                       MOVE FUNCTION NUMVAL(WS-NUM-CUENTA-STR)
                           TO NUM-CUENTA(IDX)
                       MOVE FUNCTION TRIM(WS-NOMBRE-STR)
                           TO NOMBRE-TITULAR(IDX)
                       MOVE FUNCTION NUMVAL(WS-SALDO-STR)
                           TO SALDO-ACTUAL(IDX)
               END-READ
           END-PERFORM.

       PROCESAR-MOVIMIENTOS.
           MOVE 'N' TO WS-EOF-MOVIMIENTOS.
           PERFORM UNTIL WS-EOF-MOVIMIENTOS = 'S'
               READ MOVIMIENTOS-FILE
                   AT END
                       MOVE 'S' TO WS-EOF-MOVIMIENTOS
                   NOT AT END
                       MOVE MOVIMIENTOS-RECORD(1:10) 
                           TO WS-NUM-CUENTA-STR
                       MOVE MOVIMIENTOS-RECORD(12:1) 
                           TO WS-TIPO-STR
                       MOVE MOVIMIENTOS-RECORD(14:20) 
                           TO WS-MONTO-STR
                       
                       MOVE FUNCTION NUMVAL(WS-NUM-CUENTA-STR)
                           TO WS-NUM-CUENTA-NUM
                       MOVE FUNCTION NUMVAL(WS-MONTO-STR)
                           TO WS-MONTO-NUM
                       
                       PERFORM BUSCAR-Y-ACTUALIZAR
               END-READ
           END-PERFORM.

       BUSCAR-Y-ACTUALIZAR.
           PERFORM VARYING IDX FROM 1 BY 1
               UNTIL IDX > WS-TOTAL-CUENTAS
               IF NUM-CUENTA(IDX) = WS-NUM-CUENTA-NUM
                   IF WS-TIPO-STR = 'D'
                       ADD WS-MONTO-NUM TO SALDO-ACTUAL(IDX)
                   ELSE
                       IF WS-TIPO-STR = 'R'
                           SUBTRACT WS-MONTO-NUM 
                               FROM SALDO-ACTUAL(IDX)
                       END-IF
                   END-IF
               END-IF
           END-PERFORM.

       GENERAR-REPORTE.
           MOVE 'REPORTE DE ACTUALIZACION DE SALDOS'
               TO WS-LINEA-SALIDA.
           WRITE REPORTE-RECORD FROM WS-LINEA-SALIDA.

           MOVE '================================================='
               TO WS-LINEA-SALIDA.
           WRITE REPORTE-RECORD FROM WS-LINEA-SALIDA.

           MOVE SPACES TO WS-LINEA-SALIDA.
           WRITE REPORTE-RECORD FROM WS-LINEA-SALIDA.

           MOVE 'Cuenta     | Titular               | Saldo'
               TO WS-LINEA-SALIDA.
           WRITE REPORTE-RECORD FROM WS-LINEA-SALIDA.

           MOVE '================================================='
               TO WS-LINEA-SALIDA.
           WRITE REPORTE-RECORD FROM WS-LINEA-SALIDA.

           PERFORM VARYING IDX FROM 1 BY 1
               UNTIL IDX > WS-TOTAL-CUENTAS
               MOVE SPACES TO WS-LINEA-SALIDA
               MOVE SALDO-ACTUAL(IDX) TO WS-SALDO-DISPLAY
               STRING NUM-CUENTA(IDX) DELIMITED BY SIZE
                   ' | ' DELIMITED BY SIZE
                   NOMBRE-TITULAR(IDX) DELIMITED BY '  '
                   ' | $' DELIMITED BY SIZE
                   WS-SALDO-DISPLAY DELIMITED BY SIZE
                   INTO WS-LINEA-SALIDA
               WRITE REPORTE-RECORD FROM WS-LINEA-SALIDA
           END-PERFORM.

           MOVE SPACES TO WS-LINEA-SALIDA.
           WRITE REPORTE-RECORD FROM WS-LINEA-SALIDA.
           MOVE '================================================='
               TO WS-LINEA-SALIDA.
           WRITE REPORTE-RECORD FROM WS-LINEA-SALIDA.

       FINALIZAR.
           CLOSE MAESTRO-FILE.
           CLOSE MOVIMIENTOS-FILE.
           CLOSE REPORTE-FILE.
           DISPLAY 'Procesamiento completado.'
