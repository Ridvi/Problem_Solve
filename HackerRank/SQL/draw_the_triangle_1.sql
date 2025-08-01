DELIMITER //

CREATE PROCEDURE LOOP_P()
BEGIN 
    DECLARE I INT DEFAULT 20;

    
    WHILE I>=1 DO


        SELECT REPEAT('* ',I );
            
            
        SET I=I-1;
    END WHILE  ;

END //
DELIMITER ;
CALL LOOP_P();
