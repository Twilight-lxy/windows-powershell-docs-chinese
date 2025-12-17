---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/reset-adserviceaccountpassword?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Reset-ADServiceAccountPassword
---

# 重置 ADService 账户密码

## 摘要
重置一个独立托管服务账户的密码。

## 语法

```
Reset-ADServiceAccountPassword [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-Identity] <ADServiceAccount>
 [-Partition <String>] [<CommonParameters>]
```

## 描述
`Reset-ADServiceAccountPassword` 这个 cmdlet 用于重置本地计算机上独立管理的服务账户（MSA）的密码。您必须在该独立 MSA 安装的计算机上运行此 cmdlet。对于组管理的服务账户，不支持重置密码的功能。

`Identity` 参数指定了接收密码重置操作的 Active Directory 独立 MSA（Microsoft Services Account）。您可以通过 MSA 的区分名称（DN）、GUID、安全标识符（SID）或安全帐户管理器（SAM）帐户名称来识别它。您还可以将 `Identity` 参数设置为一个 MSA 对象变量（例如 `$<localServiceAccountObject>`），或者通过管道将该 MSA 对象传递给 `Identity` 参数。例如，您可以使用 **Get-ADServiceAccount** cmdlet 获取一个独立的 MSA 对象，然后通过管道将该对象传递给 **Reset-ADServiceAccountPassword** cmdlet。

注意：当你重置一台计算机的密码时，也会同时重置该计算机上所有独立的 Microsoft Services Account（MSA）的密码。

## 示例

### 示例 1：重置独立 MSA 的密码
```
PS C:\> Reset-ADServiceAccountPassword -Identity ServiceAccount1
```

此命令用于重置独立托管服务账户ServiceAccount1的密码。

## 参数

### -AuthType
指定要使用的认证方法。该参数的可接受值包括：

- Negotiate or 0
- Basic or 1

默认的认证方法是“Negotiate”。

基本身份验证方法需要使用安全套接字层（SSL）连接。

```yaml
Type: ADAuthType
Parameter Sets: (All)
Aliases:
Accepted values: Negotiate, Basic

Required: False
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

### -Identity
通过提供以下属性值之一来指定一个 Active Directory 账户对象。括号中的标识符是该属性的轻量级目录访问协议（LDAP）显示名称。此参数的可接受值为：

- A distinguished name
- A GUID (objectGUID)
- A security identifier (objectSid)
- A SAM account name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它会返回一个无法终止的错误（即程序会持续运行而不会停止）。

这个参数也可以通过管道获取该对象，或者你可以将这个参数设置为一个对象实例。

```yaml
Type: ADServiceAccount
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Partition
指定 Active Directory 分区的唯一名称（distinguished name）。该唯一名称必须是当前目录服务器上所支持的命名上下文之一。此 cmdlet 会在此分区中搜索由 *Identity* 参数定义的对象。

在许多情况下，如果未指定值，则会为“Partition”参数使用默认值。确定默认值的规则如下所述。请注意，首先列出的规则会先被评估；一旦确定了默认值，后续的规则将不再被评估。

在 Active Directory 域服务（AD DS）环境中，以下情况下会为“分区（Partition）”设置默认值：

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If none of the previous cases apply, the default value of *Partition* is set to the default partition or naming context of the target domain.

In Active Directory Lightweight Directory Services (AD LDS) environments, a default value for *Partition* is set in the following cases:

- If the *Identity* parameter is set to a distinguished name, the default value of *Partition* is automatically generated from this distinguished name.
- If running cmdlets from an Active Directory provider drive, the default value of *Partition* is automatically generated from the current path in the drive.
- If the target AD LDS instance has a default naming context, the default value of *Partition* is set to the default naming context.
To specify a default naming context for an AD LDS environment, set the **msDS-defaultNamingContext** property of the Active Directory directory service agent object (**nTDSDSA**) for the AD LDS instance.
- If none of the previous cases apply, the *Partition* parameter does not take any default value.

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行这个cmdlet。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.ActiveDirectory.Management.ADServiceAccount
由*Identity*参数接收一个托管服务账户对象。

## 输出

### 无

## 备注
* This cmdlet does not work with Active Directory Lightweight Directory Services (AD LDS).
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

