---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/unlock-bitlocker?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Unlock-BitLocker
---

# 解锁 BitLocker

## 摘要
恢复对使用 BitLocker 加密技术保护的卷中数据的访问权限。

## 语法

### OnlyPasswordParameterSet
```
Unlock-BitLocker [-MountPoint] <String[]> -Password <SecureString> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### OnlyRecoveryPasswordParameterSet
```
Unlock-BitLocker [-MountPoint] <String[]> -RecoveryPassword <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### OnlyRecoveryKeyParameterSet
```
Unlock-BitLocker [-MountPoint] <String[]> -RecoveryKeyPath <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 只能使用 `AdAccount` 或 `Group` 作为参数
```
Unlock-BitLocker [-MountPoint] <String[]> [-AdAccountOrGroup] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
` Unlock-BitLocker ` cmdlet 可以恢复对使用 BitLocker 驱动加密技术的卷上加密数据的访问权限。而 ` Lock-BitLocker ` cmdlet 则可用于阻止对这些数据的访问。

为了恢复访问权限，请为该卷提供以下保护措施之一：

- Active Directory Domain Services (AD DS) account
- Password
- Recovery key
- Recovery password

For an overview of BitLocker, see [BitLocker Drive Encryption Overview](https://technet.microsoft.com/en-us/library/cc732774.aspx) on TechNet.

## 示例

### Example 1: Unlock a volume
```
PS C:\> $SecureString = ConvertTo-SecureString "fjuksAS1337" -AsPlainText -Force
PS C:\> Unlock-BitLocker -MountPoint "E:" -Password $SecureString
```

这个示例通过使用密码来解锁指定的 BitLocker 卷。

第一个命令使用了 **ConvertTo-SecureString** cmdlet 来创建一个包含密码的安全字符串，并将其保存在 `$SecureString` 变量中。有关 **ConvertTo-SecureString** cmdlet 的更多信息，可以输入 `Get-Help ConvertTo-SecureString` 命令查看。

第二个命令使用存储在 $SecureString 变量中的密码来解锁指定的 BitLocker 卷。

## 参数

### -AdAccountOrGroup
表示 BitLocker 需要账户凭据来解锁卷。为了使用此参数，当前用户的账户必须是该卷的密钥保护者（key protector）。

```yaml
Type: SwitchParameter
Parameter Sets: OnlyAdAccountOrGroupParameterSet
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前会提示您进行确认。

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
指定一个由驱动器字母或 BitLocker 卷对象组成的数组。此 cmdlet 会解锁所指定的卷。若要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

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
指定一个包含密码的安全字符串。所指定的密码用于保护卷加密密钥。

```yaml
Type: SecureString
Parameter Sets: OnlyPasswordParameterSet
Aliases: pw

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RecoveryKeyPath
指定存储恢复密钥的文件夹路径。如果找到了存储在该路径下的密钥，该密钥将用于保护卷的加密状态。

```yaml
Type: String
Parameter Sets: OnlyRecoveryKeyParameterSet
Aliases: rk

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -RecoveryPassword
指定一个恢复密码。该密码用于保护卷加密密钥的安全。

```yaml
Type: String
Parameter Sets: OnlyRecoveryPasswordParameterSet
Aliases: rp

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### BitLockerVolume[], String[]

## 输出

### BitLockerVolume[]

## 备注

## 相关链接

[禁用 BitLocker](./Disable-BitLocker.md)

[Enable-BitLocker](./Enable-BitLocker.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)

[Lock-BitLocker](./Lock-BitLocker.md)

[Resume-BitLocker](./Resume-BitLocker.md)

[暂停BitLocker功能](./Suspend-BitLocker.md)

