---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: BitLocker-help.xml
Module Name: BitLocker
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/bitlocker/clear-bitlockerautounlock?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Clear-BitLockerAutoUnlock
---

# Clear-BitLockerAutoUnlock

## 摘要
删除BitLocker的自动解锁密钥。

## 语法

```
Clear-BitLockerAutoUnlock [<CommonParameters>]
```

## 描述
**Clear-BitLockerAutoUnlock** cmdlet 会删除 BitLocker 驱动加密所使用的所有自动解锁密钥。BitLocker 将这些密钥存储在系统中支持 BitLocker 的操作系统所在的分区上，以便能够自动解锁系统中的固定数据驱动器和可移动数据驱动器。这样用户就可以更轻松地访问数据驱动器了。

您可以配置 BitLocker，使其自动解锁那些未安装操作系统的磁盘卷。当用户解锁了装有操作系统的磁盘卷后，BitLocker 会利用存储在注册表和磁盘元数据中的加密信息来解锁所有启用自动解锁功能的 数据磁盘卷。

在使用 **Disable-BitLocker** cmdlet 禁用 BitLocker 之前，你必须先删除自动解锁密钥。你可以使用 **Disable-BitLockerAutoUnlock** cmdlet 来仅删除特定卷的自动解锁密钥，而不是所有卷的密钥。

有关 BitLocker 的概述，请参阅 TechNet 上的 [BitLocker 磁盘加密概述](https://technet.microsoft.com/en-us/library/cc732774.aspx)。

## 示例

### 示例 1：清除自动解锁密钥
```
PS C:\>Clear-BitLockerAutoUnlock
```

这个命令会清除当前计算机上存储的所有自动解锁密钥。

## 参数

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 字符串

## 输出

### BitLockerVolume

## 备注

## 相关链接

[Disable-BitLockerAutoUnlock](./Disable-BitLockerAutoUnlock.md)

[Enable-BitLockerAutoUnlock](./Enable-BitLockerAutoUnlock.md)

[Get-BitLockerVolume](./Get-BitLockerVolume.md)

