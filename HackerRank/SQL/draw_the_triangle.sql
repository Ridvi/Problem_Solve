DELIMITER //

CREATE PROCEDURE LOOP_P()
BEGIN 
    DECLARE I INT DEFAULT 1;

    
    WHILE I<=20 DO


        SELECT REPEAT('* ',I );
            
            
        SET I=I+1;
    END WHILE  ;

END //
DELIMITER ;
CALL LOOP_P();
