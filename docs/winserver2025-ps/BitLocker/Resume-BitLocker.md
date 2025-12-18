---
description: 使用这个主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/resume-bitlocker?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Resume-BitLocker
---

# Resume-BitLocker

## 摘要
恢复指定卷的BitLocker加密功能。

## 语法

```
Resume-BitLocker [-MountPoint] <String[]> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Resume-Bitlocker` cmdlet 可以恢复使用 BitLocker 驱动加密技术的卷上的加密状态。你可以使用 `Suspend-BitLocker` cmdlet 来允许用户暂时访问已加密的数据。写入该卷的数据仍然会被加密，但用于解密操作系统卷的密钥此时处于“可用”状态（即可以被访问）。

您可以通过驱动器字母来指定一个卷，或者您可以指定一个 BitLocker 卷对象。如果您指定的 BitLocker 卷没有被挂起（即仍然处于启用状态），那么此 cmdlet 对该卷没有任何影响。

有关 BitLocker 的概述，请参阅 TechNet 上的 [BitLocker 驱动器加密概述](https://technet.microsoft.com/en-us/library/cc732774.aspx)。

## 示例

### 示例 1：对卷进行恢复保护
```
PS C:\> Resume-BitLocker -MountPoint "C:"
```

此命令会恢复C:驱动器的BitLocker保护功能。

### 示例 2：保护计算机上所有卷的数据安全
```
PS C:\>Get-BitLockerVolume | Resume-BitLocker
```

该命令使用 **Get-BitLockerVolume** cmdlet 获取当前计算机上所有的 BitLocker 加密卷，并通过管道运算符将这些加密卷传递给 **Resume-BitLocker** 命令。最终，所有 BitLocker 加密卷的保护功能都会被恢复。

## 参数

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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
指定一个驱动器字母数组或 BitLocker 卷对象。此cmdlet将恢复对所指定卷的保护。要获取 BitLocker 卷对象，请使用 **Get-BitLockerVolume** cmdlet。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### BitLockerVolume[], String[]

## 输出

### BitLockerVolume[]

## 备注

## 相关链接

[禁用BitLocker](./Disable-BitLocker.md)

[Enable-BitLocker](./Enable-Bitlocker.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)

[Lock-BitLocker](./Lock-BitLocker.md)

[暂停 BitLocker](./Suspend-BitLocker.md)

[解锁BitLocker](./Unlock-BitLocker.md)

