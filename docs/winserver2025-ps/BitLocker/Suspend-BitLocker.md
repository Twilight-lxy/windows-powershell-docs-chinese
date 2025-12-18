---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/suspend-bitlocker?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Suspend-BitLocker
---

# 暂停使用 BitLocker（数据加密技术）

## 摘要
暂停指定卷上的BitLocker加密功能。

## 语法

```
Suspend-BitLocker [-MountPoint] <String[]> [[-RebootCount] <Int32>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Suspend-BitLocker` cmdlet 用于暂停 BitLocker 加密功能，从而使用户能够访问使用 BitLocker 驱动加密技术的卷上的已加密数据。该 cmdlet 会以明文形式提供加密密钥。

暂停使用 BitLocker 并不意味着 BitLocker 会解密卷上的数据。实际上，暂停功能只是会让用于解密数据的密钥以明文形式被所有用户看到而已。新写入磁盘的数据仍然会被加密。

在挂起状态下，BitLocker 在系统启动时不会验证系统的完整性。您可以为固件升级或系统更新而暂时停用 BitLocker 的保护功能。

您可以使用 *RebootCount* 参数来指定计算机在 BitLocker 保护暂停状态结束后重新启动的次数；或者，也可以使用 **Resume-BitLocker** cmdlet 来手动恢复 BitLocker 保护。如果您没有指定 *RebootCount* 参数，该 cmdlet 会自动使用默认值“1”，这意味着 BitLocker 保护会在下一次重启后重新启用。

有关 BitLocker 的概述，请参阅 TechNet 上的 [BitLocker 磁盘加密概述](https://technet.microsoft.com/en-us/library/cc732774.aspx)。

## 示例

### 示例 1：暂停 BitLocker 保护
```
PS C:\> Suspend-BitLocker -MountPoint "C:" -RebootCount 0
```

此命令会暂停由 *MountPoint* 参数指定的 BitLocker 卷上的 Bitlocker 加密功能。由于 *RebootCount* 参数的值为 0，因此 BitLocker 加密将保持暂停状态，直到您运行 **Resume-BitLocker** cmdlet 为止。

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

### -MountPoint
用于指定一组驱动器字母或 BitLocker 卷对象。此cmdlet会暂停对所指定卷的保护功能。若要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

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

### -RebootCount
该参数指定在 BitLocker 恢复保护之前需要重新启动计算机的次数。允许的值范围是：0 到 15 之间的整数。

指定值为 0 可以无限期地暂停保护功能，直到您使用 **Resume-BitLocker** cmdlet 恢复该保护功能。

如果您不包含此参数，cmdlet 将使用值 1。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该 cmdlet 会发生什么情况。但实际上并没有运行这个 cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### BitLockerVolume[], String[]

## 输出

### BitLockerVolume[]

## 备注

## 相关链接

[禁用BitLocker](./Disable-BitLocker.md)

[Enable-BitLocker](./Enable-BitLocker.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)

[Lock-BitLocker](./Lock-BitLocker.md)

[Resume-BitLocker](./Resume-BitLocker.md)

[解锁BitLocker](./Unlock-BitLocker.md)

