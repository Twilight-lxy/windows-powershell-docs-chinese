---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: IpamDatabase.cdxml-help.xml
Module Name: IpamServer
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/ipamserver/get-ipamdatabase?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-IpamDatabase
---

# Get-IpamDatabase

## 摘要
获取IPAM数据库的配置设置。

## 语法

```
Get-IpamDatabase [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob] [<CommonParameters>]
```

## 描述
`Get-IpamDatabase` cmdlet 用于获取 IP 地址管理（IPAM）数据库的配置设置。该 cmdlet 可以获取 Windows 内部数据库（WID）或 Microsoft SQL Server 数据库的配置信息。

使用 `Set-IpamDatabase` cmdlet 来修改 IPAM 用于连接数据库的设置。

您必须是 IPAM 服务器上的本地管理员才能运行此 cmdlet。

## 示例

### 示例 1：获取 IPAM 数据库属性
```
PS C:\> Get-IpamDatabase
DatabaseType     : WID

WidSchemaPath    : C:\Windows\System32\ipam\Database

DatabaseServer   :

DatabaseName     : IPAM

DatabasePort     :

DatabaseAuthType : Windows

DatabaseUser     :
```

这个命令用于获取 IPAM 数据库的属性。在这个示例中，数据库的类型是 WID。

### 示例 2：获取外部数据库的 IPAM 数据库属性
```
PS C:\> Get-IpamDatabase
DatabaseType     : MSSQL

WidSchemaPath    :

DatabaseServer   : ContosoDB22

DatabaseName     : IpamDB1

DatabasePort     : 1433

DatabaseAuthType : Windows

DatabaseUser     :
```

这个命令用于获取外部数据库的IPAM（IP地址管理）属性。在这个示例中，数据库类型是MSSQL。

## 参数

### -AsJob
将cmdlet作为后台作业运行。使用此参数来执行需要较长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列的cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台任务的更多信息，请参阅 [关于任务（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入一个计算机名称，或者是一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获取的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases: Session

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ThrottleLimit
该参数用于指定可以同时运行的 cmdlet 操作的最大数量。如果省略了此参数或输入了 `0`，那么 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算出一个最优的节流限制。该节流限制仅适用于当前运行的 cmdlet，而不适用于整个会话或计算机本身。

```yaml
Type: Int32
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### IpamDatabase
一个对象，用于表示IPAM用来连接到数据存储库的数据库设置。

## 备注

## 相关链接

[Move-IpamDatabase](./Move-IpamDatabase.md)

[Set-IpamDatabase](./Set-IpamDatabase.md)

