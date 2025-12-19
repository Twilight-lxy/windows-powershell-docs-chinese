---
description: 使用此主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsClient-help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/revoke-hgskeyprotectoraccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Revoke-HgsKeyProtectorAccess
---

# 撤销 HGSKeyProtector 的访问权限

## 摘要
撤销监护人访问“密钥保护器”的权限。

## 语法

### InputObject
```
Revoke-HgsKeyProtectorAccess -KeyProtector <CimInstance> -Guardian <CimInstance> [<CommonParameters>]
```

### FriendlyName
```
Revoke-HgsKeyProtectorAccess -KeyProtector <CimInstance> -GuardianFriendlyName <String> [<CommonParameters>]
```

## 描述
`Revoke-HgsKeyProtectorAccess` cmdlet 可以撤销主机保护服务（Host Guardian Service）守护程序对某个密钥保护器（key protector）的访问权限。执行此操作需要拥有该密钥所有者的私钥（private signing key）。

## 示例

### 示例 1：撤销监护人访问权限
```
PS C:\> $Owner = Get-HgsGuardian -Name "Guardian11"
PS C:\> $GuardianA = Get-HgsGuardian -Name "GuardianA"
PS C:\> $GuardianB = Get-HgsGuardian -Name "GuardianB"
PS C:\> New-HgsKeyProtector -Owner $Owner -Guardians @($GuardianA, $GuardianB)
PS C:\> $Guardian04 = Get-HgsGuardian -Name "GuardianA"
PS C:\> Revoke-HgsKeyProtectorAccess -KeyProtector $KeyProtector -Guardian $Guardian04
```

第一个命令使用 **Get-HgsGuardian** cmdlet 获取名为 Guardian11 的守护对象，然后将该对象存储在 `$Owner` 变量中。

第二条和第三条命令分别创建了两个名为 GuardianA 和 GuardianB 的守护者对象。这些命令将这些守护者对象存储在 `$GuardianA` 和 `$GuardianB` 变量中。

第五条命令获取名为 GuardianA 的守护对象，并将该对象存储在 `$Guardian04` 变量中。

最后的命令撤销了存储在 **$Guardian04** 中的守护者对密钥保护器的访问权限。

## 参数

### -Guardian
指定一个监护人，以便撤销该监护人对密钥的访问权限。

```yaml
Type: CimInstance
Parameter Sets: InputObject
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -GuardianFriendlyName
为守护者指定一个友好的名称。

```yaml
Type: String
Parameter Sets: FriendlyName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -KeyProtector
指定要撤销访问权限的密钥保护器。

```yaml
Type: CimInstance
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### CimInstance#MSFT_HgsKeyProtector
`Microsoft.ManagementInfrastructure.CimInstance` 对象是一个封装类，用于显示 Windows 管理规范（WMI）对象。井号（`#`）后面的路径提供了底层 WMI 对象的命名空间和类名。

## 备注

## 相关链接

[Grant-HgsKeyProtectorAccess](./Grant-HgsKeyProtectorAccess.md)

[New-HgsKeyProtector](./New-HgsKeyProtector.md)

[Get-HgsGuardian](./Get-HgsGuardian.md)

