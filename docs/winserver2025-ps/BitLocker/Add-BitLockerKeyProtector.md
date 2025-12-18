---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/add-bitlockerkeyprotector?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-BitLockerKeyProtector
---

# Add-BitLockerKeyProtector

## 摘要
为 BitLocker 卷添加一个密钥保护器。

## 语法

### PasswordProtector
```
Add-BitLockerKeyProtector [-MountPoint] <String[]> [-PasswordProtector] [[-Password] <SecureString>] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### RecoveryPasswordProtector
```
Add-BitLockerKeyProtector [-MountPoint] <String[]> [-RecoveryPasswordProtector] [[-RecoveryPassword] <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### StartupKeyProtector
```
Add-BitLockerKeyProtector [-MountPoint] <String[]> [-StartupKeyProtector] [-StartupKeyPath] <String> [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### TpmAndStartupKeyProtector
```
Add-BitLockerKeyProtector [-MountPoint] <String[]> [-StartupKeyPath] <String> [-TpmAndStartupKeyProtector]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### TpmAndPinAndStartupKeyProtector
```
Add-BitLockerKeyProtector [-MountPoint] <String[]> [-StartupKeyPath] <String>
 [-TpmAndPinAndStartupKeyProtector] [[-Pin] <SecureString>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### SidProtector
```
Add-BitLockerKeyProtector [-MountPoint] <String[]> [-ADAccountOrGroupProtector] [-ADAccountOrGroup] <String>
 [-Service] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### TpmAndPinProtector
```
Add-BitLockerKeyProtector [-MountPoint] <String[]> [[-Pin] <SecureString>] [-TpmAndPinProtector] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### TpmProtector
```
Add-BitLockerKeyProtector [-MountPoint] <String[]> [-TpmProtector] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RecoveryKeyProtector
```
Add-BitLockerKeyProtector [-MountPoint] <String[]> [-RecoveryKeyProtector] [-RecoveryKeyPath] <String>
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-BitLockerKeyProtector` cmdlet 为使用 BitLocker 驱动器加密保护的卷的卷密钥添加一个保护机制。

当用户访问受 BitLocker 保护的驱动器时（例如在启动计算机时），BitLocker 会请求相应的密钥保护机制。用户可以输入 PIN 码，或者提供一个包含加密密钥的 USB 驱动器。BitLocker 会检索到该加密密钥，并使用它来从驱动器中读取数据。

你可以使用以下方法中的一种或几种方法的组合来创建一个密钥保护器：

- Trusted Platform Module (TPM).
BitLocker uses the computer's TPM to protect the encryption key.
If you specify this protector, users can access the encrypted drive as long as it is connected to the system board that hosts the TPM and the system boot integrity is intact.
In general, TPM-based protectors can only be associated to an operating system volume.
- TPM and Personal Identification Number (PIN).
BitLocker uses a combination of the TPM and a user-supplied PIN.
A PIN is four to twenty digits or, if you allow enhanced PINs, four to twenty letters, symbols, spaces, or numbers.
- TPM, PIN, and startup key.
BitLocker uses a combination of the TPM, a user-supplied PIN, and input from of a USB memory device that contains an external key.
- TPM and startup key.
BitLocker uses a combination of the TPM and input from of a USB memory device.
- Startup key.
BitLocker uses input from of a USB memory device that contains the external key.
- Password.
BitLocker uses a password.
- Recovery key.
BitLocker uses a recovery key stored as a specified file in a USB memory device.
- Recovery password.
BitLocker uses a recovery password.
- Active Directory Domain Services (AD DS) account.
BitLocker uses domain authentication to unlock data volumes.
Operating system volumes cannot use this type of key protector.

一次只能添加这些方法中的一种或它们的组合，但你可以在一个卷上多次运行这个cmdlet。

添加密钥保护器是一个简单的操作。例如，如果向一个使用 TPM 和 PIN 组合作为密钥保护器的卷中添加启动密钥保护器，那么实际上会创建两个独立的密钥保护器（而不是一个同时使用 TPM、PIN 和启动密钥的单一保护器）。正确的做法是先添加一个同时使用 TPM、PIN 和启动密钥的保护器，然后通过使用 **Remove-BitLockerKeyProtector** cmdlet 来移除 TPM 和 PIN 保护器。

对于密码或PIN码保护工具，请指定一个安全的字符串。您可以使用 **ConvertTo-SecureString** cmdlet 来创建这样的安全字符串。在脚本中使用这些安全字符串，仍然可以确保密码的保密性。

此cmdlet返回一个BitLocker卷对象。如果您选择“恢复密码”作为密钥保护方式，但未指定48位的恢复密码，那么该cmdlet会自动生成一个随机的48位恢复密码，并将该密码存储在BitLocker卷对象的**KeyProtector**属性的**RecoveryPassword**字段中。

如果您在密钥保护器中使用启动键或恢复键，请提供用于存储该密钥的路径。此cmdlet会将包含密钥的文件的名称存储在BitLocker卷对象中**KeyProtector**字段的**KeyFileName**字段中。

有关 BitLocker 的概述，请参阅 TechNet 上的 [BitLocker 驱动器加密概述](https://technet.microsoft.com/en-us/library/cc732774.aspx)。

## 示例

### 示例 1：添加密钥保护器
```
PS C:\>$SecureString = ConvertTo-SecureString "1234" -AsPlainText -Force
PS C:\>Add-BitLockerKeyProtector -MountPoint "C:" -Pin $SecureString -TPMandPinProtector
```

这个示例结合了TPM（Trusted Platform Module，可信平台模块）和PIN码作为加密保护机制，用于保护标识为驱动器字母C:的BitLocker卷。

第一个命令使用了 **ConvertTo-SecureString** cmdlet 来创建一个包含 PIN 的安全字符串，并将该字符串保存在 $SecureString 变量中。有关 **ConvertTo-SecureString** cmdlet 的更多信息，请输入 `Get-Help ConvertTo-SecureString`。

第二个命令为使用驱动器字母C:的BitLocker卷添加了一个保护机制。该命令指定该卷使用TPM（可信平台模块）和PIN码的组合作为密钥保护方式，并使用了存储在$SecureString变量中的PIN码。

### 示例 2：为所有使用 BitLocker 加密的卷添加恢复密钥
```
PS C:\>Get-BitLockerVolume | Add-BitLockerKeyProtector -RecoveryKeyPath "E:\Recovery\" -RecoveryKeyProtector
```

这个命令会获取当前计算机上所有的 BitLocker 加密卷，并通过管道运算符将这些卷传递给 **Add-BitLockerKeyProtector** cmdlet。该 cmdlet 指定一个文件夹路径，用于存储随机生成的恢复密钥，并表明这些加密卷使用恢复密钥作为密钥保护机制。

### 示例 3：将凭据作为密钥保护器添加
```
PS C:\>Add-BitLockerKeyProtector -MountPoint "C:" -AdAccountOrGroup "Western\SarahJones" -AdAccountOrGroupProtector
```

此命令为由 *MountPoint* 参数指定的 BitLocker 卷添加一个 AD DS 账户密钥保护器。该命令指定了一个账户，并说明 BitLocker 将使用该用户的凭据作为密钥保护器。当用户访问这个卷时，BitLocker 会要求输入用户名 Western\SarahJones 的凭据。

## 参数

### -ADAccountOrGroup
使用“Domain/User”格式指定一个账户。此cmdlet会将您指定的账户添加为卷加密密钥的密钥保护者。

```yaml
Type: String
Parameter Sets: SidProtector
Aliases: sid

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ADAccountOrGroupProtector
这表示 BitLocker 使用 AD DS 账户来保护卷加密密钥。

```yaml
Type: SwitchParameter
Parameter Sets: SidProtector
Aliases: sidp

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -MountPoint
用于指定一组驱动器字母或 BitLocker 卷对象。此 cmdlet 会为指定的卷添加一个密钥保护机制。若要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Password
指定一个包含密码的安全字符串对象。此 cmdlet 将指定的密码作为卷加密密钥的保护机制（即“保护器”）添加到系统中。

```yaml
Type: SecureString
Parameter Sets: PasswordProtector
Aliases: pw

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PasswordProtector
这表示 BitLocker 使用密码来保护卷加密密钥。

```yaml
Type: SwitchParameter
Parameter Sets: PasswordProtector
Aliases: pwp

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Pin
指定一个包含PIN码的安全字符串对象。该cmdlet会将指定的PIN码与其他数据一起添加，用作卷加密密钥的保护措施。

```yaml
Type: SecureString
Parameter Sets: TpmAndPinAndStartupKeyProtector, TpmAndPinProtector
Aliases: p

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RecoveryKeyPath
指定一个文件夹的路径。此cmdlet会生成一个随机恢复密钥，作为卷加密密钥的保护机制，并将其存储在指定的路径中。

```yaml
Type: String
Parameter Sets: RecoveryKeyProtector
Aliases: rk

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RecoveryKeyProtector
表示 BitLocker 使用恢复密钥来保护卷加密密钥。

```yaml
Type: SwitchParameter
Parameter Sets: RecoveryKeyProtector
Aliases: rkp

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RecoveryPassword
指定一个恢复密码。如果您不指定此参数，cmdlet 将生成一个随机密码。您可以输入一个 48 位长的密码。该 cmdlet 会将所指定的或生成的密码添加为卷加密密钥的保护机制。

```yaml
Type: String
Parameter Sets: RecoveryPasswordProtector
Aliases: rp

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RecoveryPasswordProtector
这表示 BitLocker 使用恢复密码来保护卷加密密钥的安全性。

```yaml
Type: SwitchParameter
Parameter Sets: RecoveryPasswordProtector
Aliases: rpp

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Service
表示该计算机的系统账户用于解锁被加密的卷（即解密该卷中的数据）。

```yaml
Type: SwitchParameter
Parameter Sets: SidProtector
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StartupKeyPath
指定一个启动密钥（startup key）的路径。该cmdlet会将存储在指定路径中的密钥添加为卷加密密钥的保护机制。

```yaml
Type: String
Parameter Sets: StartupKeyProtector, TpmAndStartupKeyProtector, TpmAndPinAndStartupKeyProtector
Aliases: sk

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StartupKeyProtector
这表示 BitLocker 使用一个启动密钥来保护卷加密密钥。

```yaml
Type: SwitchParameter
Parameter Sets: StartupKeyProtector
Aliases: skp

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TpmAndPinAndStartupKeyProtector
这表示 BitLocker 使用 TPM（可信平台模块）、PIN 码以及启动密钥的组合来保护卷加密密钥。

```yaml
Type: SwitchParameter
Parameter Sets: TpmAndPinAndStartupKeyProtector
Aliases: tpskp

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TpmAndPinProtector
这表示 BitLocker 使用 TPM（ Trusted Platform Module，可信平台模块）和 PIN 码的组合来保护卷加密密钥的安全。

```yaml
Type: SwitchParameter
Parameter Sets: TpmAndPinProtector
Aliases: tpp

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TpmAndStartupKeyProtector
这表明 BitLocker 使用 TPM（Trusted Platform Module，可信平台模块）和启动密钥的组合来保护卷加密密钥。

```yaml
Type: SwitchParameter
Parameter Sets: TpmAndStartupKeyProtector
Aliases: tskp

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TpmProtector
表示 BitLocker 使用 TPM 作为卷加密密钥的保护机制。

```yaml
Type: SwitchParameter
Parameter Sets: TpmProtector
Aliases: tpmp

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### BitLockerVolume[], string[]

## 输出

### BitLockerVolume[]

## 备注

## 相关链接

[Backup-BitLockerKeyProtector](./Backup-BitLockerKeyProtector.md)

[Enable-BitLocker](./Enable-BitLocker.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)

[Remove-BitLockerKeyProtector](./Remove-BitLockerKeyProtector.md)

