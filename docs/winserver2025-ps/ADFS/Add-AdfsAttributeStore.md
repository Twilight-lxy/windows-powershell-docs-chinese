---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/add-adfsattributestore?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Add-AdfsAttributeStore
---

# 添加 AdFS Attribute Store

## 摘要
向联邦服务（Federation Service）添加一个属性存储（attribute store）。

## 语法

### 预定义的
```
Add-AdfsAttributeStore -Name <String> -StoreType <String> -Configuration <Hashtable> [-PassThru] [-WhatIf]
 [-Confirm] [<CommonParameters>]
```

### 自定义
```
Add-AdfsAttributeStore -Name <String> -TypeQualifiedName <String> -Configuration <Hashtable> [-PassThru]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Add-AdfsAttributeStore` cmdlet 用于向联邦服务（Federation Service）添加一个属性存储（attribute store）。

## 示例

### 示例 1：添加一个用于存储 SQL 类型属性的结构
```
PS C:\> Add-AdfsAttributeStore -Name "LocalSqlStore" -StoreType "SQL" -Configuration @{"name" = "SQL Attribute Store"; "Connection" = "Server=CONTOSOSRV01;Database=UserAttributes;Integrated Security=True;Async=True"}
```

这个命令添加了一个基于 SQL 的属性存储，名为 LocalSqlStore。

### 示例 2：添加一个自定义属性存储
```
PS C:\> Add-AdfsAttributeStore -Name "MyCustomStore" -TypeQualifiedName "Contoso.CustomTypes.MyAttributeStore, Contoso.CustomTypes" -Configuration @{"Name" = "Custom Attribute Store"; "Connection" = "Default"}
```

这个命令添加了一个名为“MyCustomStore”的自定义属性存储。

## 参数

### -Configuration
指定属性存储的初始化参数，例如连接字符串。

```yaml
Type: Hashtable
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定此属性存储的友好名称（即易于理解的名称）。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -StoreType
指定要添加的属性存储类型。该参数的可接受值包括：

- ActiveDirectory
- LDAP
- SQL

```yaml
Type: String
Parameter Sets: Predefined
Aliases:
Accepted values: ActiveDirectory, LDAP, SQL

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TypeQualifiedName
Specifies the class reference for a custom attribute store that is implemented in a .NET assembly.

```yaml
Type: String
Parameter Sets: Custom
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
Prompts you for confirmation before running the cmdlet.

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

### -WhatIf
Shows what would happen if the cmdlet runs.
The cmdlet is not run.

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
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216).

## 输入

### None

## 输出

### None or Microsoft.IdentityServer.Management.Resources.AttributeStore

Returns the new AttributeStore object when the *PassThru* parameter is specified. By default, this cmdlet does not generate any output.

## 备注
* An Active Directory Federation Services (AD FS) 2.0 attribute store is a pluggable module that the policy process for AD FS 2.0 can query to retrieve claim values. You can use either an Active Directory database or a Microsoft SQL Server database as your attribute store, or you can implement your own custom attribute store.

## 相关链接

[Get-AdfsAttributeStore](./Get-AdfsAttributeStore.md)

[Set-AdfsAttributeStore](./Set-AdfsAttributeStore.md)

[Remove-AdfsAttributeStore](./Remove-AdfsAttributeStore.md)

