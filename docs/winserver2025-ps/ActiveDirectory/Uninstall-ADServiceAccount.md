---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ActiveDirectory.Management.dll-Help.xml
Module Name: ActiveDirectory
ms.date: 12/27/2016
online version: https://learn.microsoft.com/powershell/module/activedirectory/uninstall-adserviceaccount?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Uninstall-ADServiceAccount
---

# 卸载 ADServiceAccount

## 摘要
从计算机上卸载由 Active Directory 管理的服务账户，或删除计算机中缓存的组管理服务账户。

## 语法

```
Uninstall-ADServiceAccount [-WhatIf] [-Confirm] [-AuthType <ADAuthType>] [-ForceRemoveLocal]
 [-Identity] <ADServiceAccount> [<CommonParameters>]
```

## 描述
`Uninstall-ADServiceAccount` cmdlet 用于删除在运行该 cmdlet 的计算机上存在的 Active Directory 独立托管服务账户（MSA）。对于属于某个组的 MSAs，该 cmdlet 会将该组 MSA 从缓存中移除。但是，如果仍有服务正在使用该组 MSA，并且主机具有获取密码的权限，那么系统会创建一个新的缓存条目。需要注意的是，指定的 MSA 必须已经安装在相应的计算机上。

`Identity` 参数用于指定要卸载的 Active Directory MSA（Microsoft Service Account）。您可以通过 MSA 的唯一名称（DN）、GUID、安全标识符（SID）或安全账户管理器（SAM）帐户名称来识别它。您还可以将该参数设置为某个 MSA 对象变量（例如 `$<localServiceAccountObject>`），或者将 MSA 对象通过管道传递给 `Identity` 参数。例如，您可以使用 **Get-ADServiceAccount** cmdlet 获取一个 MSA 对象，然后将该对象通过管道传递给 **Uninstall-ADServiceAccount** cmdlet 进行卸载操作。

## 示例

### 示例 1：卸载指定的 MSA
```
PS C:\> Uninstall-ADServiceAccount -Identity SQL-SRV1
```

该命令会从本地计算机上卸载被识别为SQL-SRV1的MSA（Microsoft SQL Server Agent）。

### 示例 2：从只读域控制器站点中的服务器卸载 MSA
```
PS C:\> Uninstall-ADServiceAccount -Identity sql-hr-01 -ForceRemoveLocal
```

此命令用于从位于只读域控制器站点（例如边界网络）中的服务器上卸载指定的独立MSA（Microsoft SQL Server Analysis Services）。

## 参数

### -AuthType
指定要使用的身份验证方法。该参数的可接受值包括：

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

### -ForceRemoveLocal
这表示：如果无法访问可写域控制器，您可以将该账户从本地安全机构（LSA）中删除。当您从位于分段网络中的服务器上卸载 MSA 时（例如只能访问只读域控制器的边界网络），就需要执行此操作。如果您指定了该参数，但服务器能够访问可写域控制器，那么该账户也会从目录中的计算机账户中被解除关联。

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

### -Identity
通过提供以下属性值之一来指定一个 Active Directory 账户对象。括号中的标识符是该属性的 LDAP 显示名称。此参数的可接受值为：

- A Distinguished Name
- A GUID (objectGUID)
- A Security Identifier (objectSid)
- A SAM Account Name (sAMAccountName)

该cmdlet会在默认的命名上下文或分区中搜索相应的对象。如果找到两个或多个对象，它将返回一个表示无法继续执行的错误信息（即非终止性错误）。

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

### -WhatIf
展示了如果该cmdlet被运行会发生的结果。但实际上，这个cmdlet并没有被运行。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### 无值或 Microsoft.ActiveDirectory.Management_ADServiceAccount
通过 *Identity* 参数接收一个托管服务账户对象。提供了一个名为 **ForceRemoveLocal** 的参数，用于卸载位于只读域控制器站点上的独立托管服务账户（MSA）。

## 输出

### 无

## 备注
* This cmdlet does not work with AD LDS.
* This cmdlet does not work with an Active Directory snapshot.
* This cmdlet does not work with a read-only domain controller.

## 相关链接

[Get-ADServiceAccount](./Get-ADServiceAccount.md)

[安装 AD 服务帐户](./Install-ADServiceAccount.md)

[New-ADServiceAccount](./New-ADServiceAccount.md)

[Remove-ADServiceAccount](./Remove-ADServiceAccount.md)

[Set-ADServiceAccount](./Set-ADServiceAccount.md)

