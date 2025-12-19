---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsClient-help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/new-hgskeyprotector?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-HgsKeyProtector
---

# 新HgsKeyProtector

## 摘要
创建一个密钥保护器。

## 语法

```
New-HgsKeyProtector [-Owner] <CimInstance> [[-Guardian] <CimInstance[]>] [-AllowExpired] [-AllowUntrustedRoot]
 [<CommonParameters>]
```

## 描述
`New-HgsKeyProtector` cmdlet 用于创建一个密钥保护器。该 cmdlet 会生成一个密钥，并将其封装后交由指定的监护人所有者管理。您无法更改这个密钥保护器的所有者。您可以使用 `Grant-HgsKeyProtectorAccess` 和 `Revoke-HgsKeyProtectorAccess` cmdlets 来授予或撤销其他监护人对该密钥的访问权限。

此 cmdlet 可以根据现有密钥保护器的原始字节流来创建一个新的密钥保护器。

## 示例

### 示例 1：创建一个密钥保护器
```
PS C:\> $Owner = Get-HgsGuardian -Name "Guardian11"
PS C:\> $GuardianA = Get-HgsGuardian -Name "GuardianA"
PS C:\> $GuardianB = Get-HgsGuardian -Name "GuardianB"
PS C:\> New-HgsKeyProtector -Owner $Owner -Guardians @($GuardianA, $GuardianB)
```

第一个命令使用 **Get-HgsGuardian** cmdlet 获取名为 Guardian11 的守护对象，然后将该对象存储在 **$Owner** 变量中。

第二和第三条命令分别创建了两个守护者，名称分别为 GuardianA 和 GuardianB。这些命令将这两个守护者存储在 `$GuardianA` 和 `$GuardianB` 变量中。

最后一个命令用于创建一个密钥保护机制。该命令将 Guardian11 视为“所有者”（Owner），并同时授予对存储在 $GuardianA 和 $GuardianB 中的守护程序（guardians）的访问权限。

## 参数

### -AllowExpired
表示此cmdlet可以使用已过期的证书来创建密钥保护器。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AllowUntrustedRoot
表示此cmdlet可以使用自签名证书来创建密钥保护器。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Guardian
指定一个守护者数组，除了由 **Owner** 参数指定的守护者之外，这些守护者也可以被授权访问该密钥。

```yaml
Type: CimInstance[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Owner
为新密钥保护器指定一个监护人。该cmdlet会授予该监护人相应的访问权限。对于这个特定的密钥保护器而言，其监护人是无法被更改的。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### CimInstance#MSFT_HgsKeyProtector
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个包装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Grant-HgsKeyProtectorAccess](./Grant-HgsKeyProtectorAccess.md)

[Revoke-HgsKeyProtectorAccess](./Revoke-HgsKeyProtectorAccess.md)

[Get-HgsGuardian](./Get-HgsGuardian.md)

