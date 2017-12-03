from protorpc import messages

class Response(messages.Message):
    status = messages.StringField(1)

class MemberRequest(messages.Message):
    id_number = messages.StringField(1)
    ch_name = messages.StringField(2)
    en_name = messages.StringField(3)
    birthday = messages.StringField(4)
    nationality = messages.StringField(5)
    tel_code = messages.StringField(6)
    mobile_phone = messages.StringField(7)
    email = messages.StringField(8)
    postal_code = messages.IntegerField(9)
    address = messages.StringField(10)
    company = messages.StringField(11)
    job_title = messages.StringField(12)
    company_tel_code = messages.StringField(13)
    emergency_contact_name = messages.StringField(14)
    emergency_contact_phone = messages.StringField(15)
    source = messages.StringField(16)
    remarks = messages.StringField(17)
    blood_type = messages.StringField(18)
    left_eye = messages.StringField(19)
    right_eye = messages.StringField(20)
    height = messages.IntegerField(21)
    weight = messages.IntegerField(22) 
    ## Member equipment
    mirror = messages.BooleanField(24)
    breathing_tube = messages.BooleanField(25)
    jackets = messages.BooleanField(26)
    gloves = messages.BooleanField(27)
    overshoes = messages.BooleanField(28)
    fins = messages.BooleanField(29)
    bc = messages.BooleanField(30)
    regulator = messages.BooleanField(31)
    dive_computer = messages.BooleanField(32)
    counterweight = messages.IntegerField(33)
    ## Open Water
    owd_deposit = messages.BooleanField(34)
    owd_payment = messages.BooleanField(35)
    owd_material = messages.BooleanField(36)
    owd_apply = messages.BooleanField(37)
    owd_license = messages.BooleanField(38)
    owd_status = messages.StringField(39)
    owd_tank_card = messages.StringField(40)
    ## Advanced Adventurer 
    aa_deposit = messages.BooleanField(41)
    aa_payment = messages.BooleanField(42)
    aa_material = messages.BooleanField(43)
    aa_apply = messages.BooleanField(44)
    aa_license = messages.BooleanField(45)
    aa_status = messages.StringField(46)
    ## Nitrox - EAN
    ean_deposit = messages.BooleanField(47)
    ean_payment = messages.BooleanField(48)
    ean_material = messages.BooleanField(49)
    ean_apply = messages.BooleanField(50)
    ean_license = messages.BooleanField(51)
    ean_status = messages.StringField(52)
    ## Deep Diving - DD
    dd_deposit = messages.BooleanField(53)
    dd_payment = messages.BooleanField(54)
    dd_material = messages.BooleanField(55)
    dd_apply = messages.BooleanField(56)
    dd_license = messages.BooleanField(57)
    dd_status = messages.StringField(58)
    ## Night & Limited Visibility Diving - NL
    nl_deposit = messages.BooleanField(59)
    nl_payment = messages.BooleanField(60)
    nl_material = messages.BooleanField(61)
    nl_apply = messages.BooleanField(62)
    nl_license = messages.BooleanField(63)
    nl_status = messages.StringField(64)
    ## Navigation - NV
    nv_deposit = messages.BooleanField(65)
    nv_payment = messages.BooleanField(66)
    nv_material = messages.BooleanField(67)
    nv_apply = messages.BooleanField(68)
    nv_license = messages.BooleanField(69)
    nv_status = messages.StringField(70)
    ## Recreational Sidemount
    sidemount_deposit = messages.BooleanField(71)
    sidemount_payment = messages.BooleanField(72)
    sidemount_material = messages.BooleanField(73)
    sidemount_apply = messages.BooleanField(74)
    sidemount_license = messages.BooleanField(75)
    sidemount_status = messages.StringField(76)
    ## React Right + Stress & Rescue
    rrsr_deposit = messages.BooleanField(77)
    rrsr_payment = messages.BooleanField(78)
    rrsr_material = messages.BooleanField(79)
    rrsr_apply = messages.BooleanField(80)
    rrsr_license = messages.BooleanField(81)
    rrsr_status = messages.StringField(82)
    ## Boat Diving - BD
    bd_deposit = messages.BooleanField(83)
    bd_payment = messages.BooleanField(84)
    bd_material = messages.BooleanField(85)
    bd_apply = messages.BooleanField(86)
    bd_license = messages.BooleanField(87)
    bd_status = messages.StringField(88)
    ## Search and Recovery Diving - REC
    rec_deposit = messages.BooleanField(89)
    rec_payment = messages.BooleanField(90)
    rec_material = messages.BooleanField(91)
    rec_apply = messages.BooleanField(92)
    rec_license = messages.BooleanField(93)
    rec_status = messages.StringField(94)
    ## Free Diving - FD
    fd_deposit = messages.BooleanField(95)
    fd_payment = messages.BooleanField(96)
    fd_material = messages.BooleanField(97)
    fd_apply = messages.BooleanField(98)
    fd_license = messages.BooleanField(99)
    fd_status = messages.StringField(100)
    ## Dry Suit - DRY
    dry_deposit = messages.BooleanField(101)
    dry_payment = messages.BooleanField(102)
    dry_material = messages.BooleanField(103)
    dry_apply = messages.BooleanField(104)
    dry_license = messages.BooleanField(105)
    dry_status = messages.StringField(106)
    ## Perfect Buoyancy - PB
    pb_deposit = messages.BooleanField(107)
    pb_payment = messages.BooleanField(108)
    pb_material = messages.BooleanField(109)
    pb_apply = messages.BooleanField(110)
    pb_license = messages.BooleanField(111)
    pb_status = messages.StringField(112)
    ## DC
    dc_deposit = messages.BooleanField(113)
    dc_payment = messages.BooleanField(114)
    dc_material = messages.BooleanField(115)
    dc_apply = messages.BooleanField(116)
    dc_license = messages.BooleanField(117)
    dc_status = messages.StringField(118)
    ## ITC
    itc_deposit = messages.BooleanField(119)
    itc_payment = messages.BooleanField(120)
    itc_material = messages.BooleanField(121)
    itc_apply = messages.BooleanField(122)
    itc_license = messages.BooleanField(123)
    itc_status = messages.StringField(124)
    ## Night SPI
    nightspi_deposit = messages.BooleanField(125)
    nightspi_payment = messages.BooleanField(126)
    nightspi_material = messages.BooleanField(127)
    nightspi_apply = messages.BooleanField(128)
    nightspi_license = messages.BooleanField(129)
    nightspi_status = messages.StringField(130)