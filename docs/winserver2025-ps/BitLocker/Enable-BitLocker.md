---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/14/2021
online version: https://learn.microsoft.com/powershell/module/bitlocker/enable-bitlocker?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-BitLocker
---

# 启用 BitLocker（数据加密保护）

## 摘要

为某个卷启用 BitLocker 磁盘加密功能。

## 语法

### PasswordProtector

```PowerShell
Enable-BitLocker [-MountPoint] <String[]> -PasswordProtector [-Password] <SecureString>
[-EncryptionMethod <BitLockerVolumeEncryptionMethodOnEnable>] [-HardwareEncryption]
[-SkipHardwareTest] [-UsedSpaceOnly][-WhatIf] [-Confirm] [<CommonParameters>]
```

### RecoveryPasswordProtector

```PowerShell
Enable-BitLocker [-MountPoint] <String[]> -RecoveryPasswordProtector [[-RecoveryPassword] <String>]
[-EncryptionMethod <BitLockerVolumeEncryptionMethodOnEnable>] [-HardwareEncryption]
[-SkipHardwareTest] [-UsedSpaceOnly] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### StartupKeyProtector

```PowerShell
Enable-BitLocker [-MountPoint] <String[]> -StartupKeyProtector [-StartupKeyPath] <String>
[-EncryptionMethod <BitLockerVolumeEncryptionMethodOnEnable>] [-HardwareEncryption]
[-SkipHardwareTest] [-UsedSpaceOnly] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### TpmAndStartupKeyProtector

```PowerShell
Enable-BitLocker [-MountPoint] <String[]> -TpmAndStartupKeyProtector [-StartupKeyPath] <String>
[-EncryptionMethod <BitLockerVolumeEncryptionMethodOnEnable>] [-HardwareEncryption]
[-SkipHardwareTest] [-UsedSpaceOnly] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### TpmAndPinAndStartupKeyProtector

```PowerShell
Enable-BitLocker [-MountPoint] <String[]> -TpmAndPinAndStartupKeyProtector -StartupKeyPath <String>
[-Pin] <SecureString> [-EncryptionMethod <BitLockerVolumeEncryptionMethodOnEnable>]
[-HardwareEncryption] [-SkipHardwareTest] [-UsedSpaceOnly] [-WhatIf] [-Confirm]
[<CommonParameters>]
```

### AdAccountOrGroupProtector

```PowerShell
Enable-BitLocker [-MountPoint] <String[]> -AdAccountOrGroupProtector [-AdAccountOrGroup] <String>
[-Service] [-EncryptionMethod <BitLockerVolumeEncryptionMethodOnEnable>] [-HardwareEncryption]
[-SkipHardwareTest] [-UsedSpaceOnly] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### TpmAndPinProtector

```PowerShell
Enable-BitLocker [-MountPoint] <String[]> -TpmAndPinProtector [-Pin] <SecureString>
[-EncryptionMethod <BitLockerVolumeEncryptionMethodOnEnable>] [-HardwareEncryption]
[-SkipHardwareTest] [-UsedSpaceOnly] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### TpmProtector

```PowerShell
Enable-BitLocker [-MountPoint] <String[]> -TpmProtector
[-EncryptionMethod <BitLockerVolumeEncryptionMethodOnEnable>] [-HardwareEncryption]
[-SkipHardwareTest] [-UsedSpaceOnly] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RecoveryKeyProtector

```PowerShell
Enable-BitLocker [-MountPoint] <String[]> -RecoveryKeyProtector [-RecoveryKeyPath] <String>
[-EncryptionMethod <BitLockerVolumeEncryptionMethodOnEnable>] [-HardwareEncryption]
[-SkipHardwareTest] [-UsedSpaceOnly] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述

`Enable-BitLocker` cmdlet 可以为一个卷启用 BitLocker 磁盘加密功能。

当你启用加密功能时，必须指定一个卷，可以通过其驱动器字母或BitLocker卷对象来标识该卷。

您还需要设置一个密钥保护器。BitLocker 使用密钥保护器来加密卷的加密密钥。当用户访问受 BitLocker 加密的驱动器（例如在启动计算机时），BitLocker 会请求相关的密钥保护器。用户可以输入 PIN 码，或者提供包含密钥的 USB 驱动器。BitLocker 会解密该加密密钥，并使用它从驱动器中读取数据。您可以使用以下方法中的一种或多种组合来设置密钥保护器：

- **Trusted Platform Module (TPM):** BitLocker uses the computer's TPM to protect the encryption
  key. If you select this key protector, users can access the encrypted drive as long as it is
  connected to the system board that hosts the TPM and system boot integrity is intact. In general,
  TPM-based protectors can only be associated to an operating system volume.

- **TPM and Personal Identification Number (PIN):** BitLocker uses a combination of the TPM and a
  user-supplied PIN. A PIN is four to twenty digits or, if you allow enhanced PINs, is four to
  twenty letters, symbols, spaces, or numbers.

- **TPM, PIN, and startup key:** BitLocker uses a combination of the TPM, a user-supplied PIN, and
  input from of a USB memory device that contains an external key.

- **TPM and startup key:** BitLocker uses a combination of the TPM and a USB flash drive that
  contains the external key.

- **Startup key:** BitLocker uses a USB flash drive that contains the external key.

- **Password:** BitLocker uses a password.

- **Recovery key:** BitLocker uses a recovery key stored as a specified file.

- **Recovery password:** BitLocker uses a recovery password.

- **Active Directory Domain Services (AD DS) account:** BitLocker uses domain authentication.

在启用加密时，您只能指定这些方法中的一种或它们的组合，但可以使用 **Add-BitLockerKeyProtector** cmdlet 来添加其他保护机制。

对于密码或PIN码保护工具，请指定一个安全的字符串。您可以使用 **ConvertTo-SecureString** cmdlet 来创建这样的安全字符串。在脚本中使用这些安全字符串，仍然可以确保密码的保密性。

我们强烈建议指定加密方法。默认情况下，BitLocker 使用 XTS-AES-128；您可以选择 XTS-AES-256 以获得更强的安全性。但是，如果您要加密可移动介质，并计划在 Windows 8.1 或 Windows Server 2012 R2 上使用该介质，则必须选择 AES-128 或 AES-256 以确保向后兼容性。您可以申请使用硬件加密功能，但我们强烈不建议这样做。有关更多指导，请参阅 [ADV180028 安全公告](https://msrc.microsoft.com/update-guide/vulnerability/ADV180028)。

此cmdlet返回一个BitLocker卷对象。如果您选择“恢复密码”作为密钥保护方式，但未指定48位的恢复密码，该cmdlet会为您生成一个随机密码，并将其存储在BitLocker卷对象的**KeyProtector**属性的**RecoveryPassword**字段中。

如果您在密钥保护器中使用启动键（startup key）或恢复键（recovery key），请提供用于存储该密钥的路径。此 cmdlet 会将包含密钥的文件的名称存储在 BitLocker 卷对象中 **KeyProtector** 字段的 **KeyFileName** 字段中。

如果你在已加密的卷或正在加密过程中的卷上使用 `Enable-BitLocker` cmdlet，该命令将不会产生任何效果。如果你在暂停了加密操作的卷上使用此 cmdlet，它会恢复对该卷的加密过程。

默认情况下，此 cmdlet 会加密整个驱动器。如果您使用 *UsedSpaceOnly* 参数，则只会加密磁盘上已使用的空间。这个选项可以显著缩短加密所需的时间。

通常的做法是使用 **Add-BitlockerKeyProtector** cmdlet 为操作系统卷添加恢复密码，然后使用 **Backup-BitLockerKeyProtector** cmdlet 保存该恢复密码，最后在该卷上启用 BitLocker。这样的操作可以确保你拥有一个恢复数据的选择。

有关 BitLocker 的概述，请参阅[BitLocker 磁盘加密概述](/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc732774(v=ws.11))。

## 示例

### 示例 1：启用 BitLocker

```PowerShell
$SecureString = ConvertTo-SecureString "1234" -AsPlainText -Force
Enable-BitLocker -MountPoint "C:" -EncryptionMethod Aes256 -UsedSpaceOnly -Pin $SecureString -TPMandPinProtector
```

这个示例允许使用TPM（可信平台模块）和PIN码作为密钥保护机制，为指定的驱动器启用BitLocker功能。

第一个命令使用了 **ConvertTo-SecureString** cmdlet 来创建一个包含 PIN 的安全字符串，并将该字符串保存在 `$SecureString` 变量中。有关 **ConvertTo-SecureString** cmdlet 的更多信息，请输入 `Get-Help ConvertTo-SecureString`。

第二个命令为驱动器字母为 C: 的 BitLocker 卷启用 BitLocker 加密功能。该 cmdlet 指定了加密算法以及存储在 $SecureString 变量中的 PIN 码。同时，该命令还规定此卷使用 TPM（可信平台模块）和 PIN 码的组合作为加密保护机制。此外，该命令指示仅对磁盘上已使用的空间数据进行加密，而不是对整个卷进行加密。当系统将来向该卷写入数据时，这些数据将会被自动加密。

### 示例 2：使用恢复密钥启用 BitLocker

```PowerShell
Get-BitLockerVolume | Enable-BitLocker -EncryptionMethod Aes128 -RecoveryKeyPath "E:\Recovery\" -RecoveryKeyProtector
```

这个命令会获取当前计算机上的所有 BitLocker 加密卷，并通过管道运算符将这些加密卷传递给 **Enable-BitLocker** cmdlet。该 cmdlet 为这些加密卷指定相应的加密算法，同时还会指定一个用于存储随机生成的恢复密钥的文件夹路径，并说明这些加密卷使用恢复密钥作为数据保护机制。

### 示例 3：使用指定的用户账户启用 BitLocker

```PowerShell
Enable-BitLocker -MountPoint "C:" -EncryptionMethod Aes128 -AdAccountOrGroup "Western\SarahJones" -AdAccountOrGroupProtector
```

此命令会加密由 *MountPoint* 参数指定的 BitLocker 卷，并使用 AES 128 加密算法。该命令还指定了一个账户，并说明 BitLocker 将使用用户的凭据作为密钥保护机制。当用户访问该卷时，BitLocker 会要求用户提供 Western\SarahJones 账户的凭据。

## 参数

### -AdAccountOrGroup

使用“Domain\User”格式指定一个账户。此cmdlet会将您指定的账户添加为卷加密密钥的密钥保护者（key protector）。

```yaml
Type: String
Parameter Sets: AdAccountOrGroupProtector
Aliases: sid

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AdAccountOrGroupProtector

这表示 BitLocker 使用 AD DS 账户来保护卷加密密钥。

```yaml
Type: SwitchParameter
Parameter Sets: AdAccountOrGroupProtector
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

### -EncryptionMethod

指定用于加密驱动器的加密方法。如需更多指导，请参阅[ADV180028安全建议](https://msrc.microsoft.com/update-guide/vulnerability/ADV180028)。

```yaml
Type: BitLockerVolumeEncryptionMethodOnEnable
Parameter Sets: (All)
Aliases:
Accepted values: Aes128, Aes256, XtsAes128, XtsAes256

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HardwareEncryption

这表示该卷使用了硬件加密功能。我们强烈建议不要使用硬件加密。有关更多指导信息，请参阅[ADV180028安全公告](https://msrc.microsoft.com/update-guide/vulnerability/ADV180028)。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -MountPoint

指定一个包含驱动器字母或 BitLocker 卷对象的数组。此 cmdlet 可为指定的卷提供保护功能。若要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

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

指定一个包含密码的安全字符串对象。该密码用于保护卷加密密钥的安全性。

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

表示 BitLocker 使用密码来保护卷加密密钥。

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

指定一个包含PIN码的安全字符串对象。BitLocker会使用该PIN码以及其他数据来保护卷加密密钥。

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

指定一个文件夹的路径。此cmdlet会生成一个随机恢复密钥，用作卷加密密钥的保护机制，并将该密钥存储在指定的路径中。

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

这表明 BitLocker 使用恢复密钥来保护卷加密密钥的安全性。

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

指定一个恢复密码。如果您没有指定此参数，但指定了 *RecoveryPasswordProtector* 参数，那么该 cmdlet 将会生成一个随机密码。您可以输入一个由 48 位字符组成的密码。所指定的或生成的密码将用于保护卷加密密钥的安全性。

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

这表示 BitLocker 使用恢复密码来保护卷加密密钥。

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

表示这台计算机的系统账户用于解锁已加密的卷（即解密该卷中的数据）。

```yaml
Type: SwitchParameter
Parameter Sets: AdAccountOrGroupProtector
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -SkipHardwareTest

这表示 BitLocker 在开始加密之前不会执行硬件测试。BitLocker 会利用硬件测试作为预演，以确保所有的密钥保护机制都已正确配置，并且计算机能够顺利启动而不会出现任何问题。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: s

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -StartupKeyPath

指定一个启动密钥（startup key）的路径。存储在该路径中的密钥用于保护卷加密密钥（volume encryption key）。

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

表示 BitLocker 使用启动密钥来保护卷加密密钥。

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

这表明 BitLocker 使用 TPM（可信平台模块）、PIN 码和启动密钥的组合来保护卷加密密钥。

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

这表示 BitLocker 使用 TPM（可信平台模块）和 PIN 码的组合来保护卷加密密钥。

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

这表示 BitLocker 使用 TPM（可信平台模块）和启动密钥的组合来保护卷加密密钥。

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

表示 BitLocker 使用 Trusted Platform Module（TPM）来保护卷加密密钥的安全性。

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

### -UsedSpaceOnly

表示 BitLocker 不会对未分配的磁盘空间进行加密。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: qe

Required: False
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

### BitLockerVolume[], String[]

## 输出

### BitLockerVolume[]

## 备注

## 相关链接

[禁用BitLocker](./Disable-BitLocker.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)

[Lock-BitLocker](./Lock-BitLocker.md)

[Resume-BitLocker](./Resume-BitLocker.md)

[暂停 BitLocker 功能](./Suspend-BitLocker.md)

[解锁 BitLocker](./Unlock-BitLocker.md)
