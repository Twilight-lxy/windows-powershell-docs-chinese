---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/remove-bitlockerkeyprotector?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-BitLockerKeyProtector
---

# 移除 BitLocker 密钥保护器

## 摘要
删除BitLocker卷的关键保护机制。

## 语法

```
Remove-BitLockerKeyProtector [-MountPoint] <String[]> [-KeyProtectorId] <String> [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-BitLockerKeyProtector` cmdlet 用于移除受 BitLocker 驱动器加密保护的卷所使用的密钥保护器。

您可以使用ID来指定要删除的密钥保护器。若要添加保护器，请使用**Add-BitLockerKeyProtector** cmdlet。

如果你删除了BitLocker卷的所有密钥保护机制，那么BitLocker会以不使用加密的方式存储该卷的数据加密密钥。这意味着任何能够访问该卷的用户都可以读取其中的数据（即使这些数据是加密的），除非你重新添加密钥保护机制。驱动器上的所有加密数据仍然保持加密状态。

我们建议您至少设置一个恢复密码，作为保护卷数据的关键手段，以防您需要恢复系统时使用。

有关 BitLocker 的概述，请参阅 [BitLocker 设备加密的概述](/windows/security/information-protection/bitlocker/bitlocker-device-encryption-overview-windows-10)。

## 示例

### 示例 1：移除某个卷的第二个键保护器
```powershell
PS C:\> $BLV = Get-BitLockerVolume -MountPoint "C:"
PS C:\> Remove-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId $BLV.KeyProtector[1].KeyProtectorId
```

这个示例会移除指定BitLocker卷的关键保护机制（即用于保护该卷数据的加密措施）。

第一个命令使用 **Get-BitLockerVolume** 来获取一个 BitLocker 卷，并将其存储在 `$BLV` 变量中。

第二个命令会删除由 **MountPoint** 参数指定的 BitLocker 卷的密钥保护机制。该命令通过使用密钥保护机制的 ID 来识别它，这个 ID 存储在 `$BLV` 中的 BitLocker 对象中。

### 示例 2：移除卷上的 TpmPin 密钥保护机制
```powershell
PS C:\> $BLV = Get-BitlockerVolume -MountPoint "C:"
PS C:\> $TpmPinKeyProtector = $BLV.KeyProtector | Where-Object {$PSItem.KeyProtectorType -eq "TpmPin"}
PS C:\> Remove-BitLockerKeyProtector -MountPoint "C:" -KeyProtectorId $TpmPinKeyProtector.KeyProtectorId
```

这个示例会移除指定 BitLocker 卷中的一种类型为 TpmPin 的密钥保护机制。

第一个命令使用 **Get-BitLockerVolume** 来获取一个 BitLocker 卷，并将其存储在 `$BLV` 变量中。

第二个命令会过滤掉那些用于保护密钥的工具（key protectors），仅保留类型为 TpmPin 的那个，并将其存储在 `$TpmPinKeyProtector` 变量中。

第三个命令通过键的ID来移除键保护器。

## 参数

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

### -KeyProtectorId
用于指定密钥保护器的ID。BitLocker卷对象包含一个**KeyProtector**对象，因此必须指定该密钥保护器的ID。请参阅“示例”部分。要获取BitLocker卷对象，请使用**Get-BitLockerVolume** cmdlet。

```yaml
Type: String
Parameter Sets: (All)
Aliases: id

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -MountPoint
指定一个包含驱动器字母或 BitLocker 卷对象的数组。该 cmdlet 会删除所指定卷的密钥保护机制。要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

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

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：`-Debug`、`-ErrorAction`、`-ErrorVariable`、`-InformationAction`、`-InformationVariable`、`-OutVariable`、`-OutBuffer`、`-PipelineVariable`、`-Verbose`、`-WarningAction` 和 `-WarningVariable`。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### BitLockerVolume[], String[]

## 输出

### BitLockerVolume[]

## 备注

## 相关链接

[Add-BitLockerKeyProtector](./Add-BitLockerKeyProtector.md)

[Backup-BitLockerKeyProtector](./Backup-BitLockerKeyProtector.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)
