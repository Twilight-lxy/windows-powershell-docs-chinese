---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: MSFT_DtcTask_v1.0.cdxml-help.xml
Module Name: MsDtc
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/msdtc/stop-dtc?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-Dtc
---

# 停止 DTC（Data Center Control）

## 摘要
停止一个DTC（诊断 trouble code）实例。

## 语法

```
Stop-Dtc [-DtcName <String>] [-Recursive] [-CimSession <CimSession[]>] [-ThrottleLimit <Int32>] [-AsJob]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Stop-Dtc` cmdlet 用于停止由参数 `DtcName` 指定的分布式事务协调器（DTC）实例。

## 示例

### 示例 1：停止一个本地的 DTC 实例
```
This command uses the **Get-Dtc** cmdlet to view the status of the local DTC instance.
PS C:\> Get-Dtc -DtcName "Local"
__GENUS           : 2
__CLASS           : DtcInstance
__SUPERCLASS      :
__DYNASTY         : DtcInstance
__RELPATH         :
__PROPERTY_COUNT  : 7
__DERIVATION      : {}
__SERVER          :
__NAMESPACE       :
__PATH            :
DtcName           : Local
KtrmEndpointCid   : b6628c9f-46ff-404d-a0fa-62657cb828af
OleTxEndpointCid  : f3027ea1-4ee5-45b5-a01c-06f41221111b
Status            : Started
UisEndpointCid    : e9385758-8092-4dd7-8b09-587aa427a58e
VirtualServerName : Contoso093
XAEndpointCid     : ced49d85-82a9-49d9-a6ee-8c5b4bd7b5bd

This command stops the local DTC instance. The first command shows that the instance is started, and, therefore, it is safe to stop that instance.
PS C:\> Stop-Dtc -DtcName "Local"

This command uses **Get-Dtc**, again, to confirm that the DTC instance is stopped.
PS C:\> Get-Dtc -DtcName "Local"
__GENUS           : 2
__CLASS           : DtcInstance
__SUPERCLASS      :
__DYNASTY         : DtcInstance
__RELPATH         :
__PROPERTY_COUNT  : 7
__DERIVATION      : {}
__SERVER          :
__NAMESPACE       :
__PATH            :
DtcName           : Local
KtrmEndpointCid   : b6628c9f-46ff-404d-a0fa-62657cb828af
OleTxEndpointCid  : f3027ea1-4ee5-45b5-a01c-06f41221111b
Status            : Stopped
UisEndpointCid    : e9385758-8092-4dd7-8b09-587aa427a58e
VirtualServerName : Contoso093
XAEndpointCid     : ced49d85-82a9-49d9-a6ee-8c5b4bd7b5bd
```

这个示例用于停止本地的 DTC（ Distributed Transaction Coordinator，分布式事务协调器）实例。如果要停止其他实例，请为 **DtcName** 参数指定不同的值。

## 参数

### -AsJob
以后台作业的方式运行该cmdlet。使用此参数来执行需要很长时间才能完成的命令。

该cmdlet会立即返回一个表示作业的对象，然后显示命令提示符。在作业完成之前，您可以继续在该会话中工作。要管理作业，请使用`*-Job`系列cmdlets；要获取作业结果，请使用[Receive-Job](https://go.microsoft.com/fwlink/?LinkID=113372) cmdlet。

有关 Windows PowerShell 后台作业的更多信息，请参阅 [关于作业（About Jobs）](https://go.microsoft.com/fwlink/?LinkID=113251)。

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
在远程会话或远程计算机上运行该cmdlet。请输入一个计算机名称或会话对象（例如，[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967) 或 [Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet 的输出结果）。默认值是本地计算机上的当前会话。

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

### -DtcName
指定要停止的DTC（分布式事务协调器）实例。如果您不指定此参数，或者指定了“Local”值，此cmdlet将停止本地的DTC实例。

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

### -Recursive
表示该 cmdlet 会停止所有依赖于指定 DTC 实例的服务（例如 Microsoft SQL Server）。

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

### -ThrottleLimit
该参数用于指定可以同时执行的操作的最大数量。如果省略此参数或输入值 `0`，则 Windows PowerShell® 会根据计算机上正在运行的 CIM cmdlet 的数量来计算该 cmdlet 的最佳限制值。此限制仅适用于当前正在执行的 cmdlet，而不适用于整个会话或计算机本身。

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

### -WhatIf
展示了如果该cmdlet被运行会会发生什么情况。但实际上这个cmdlet并没有被运行。

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

## 输出

## 备注

## 相关链接

[Get-Dtc](./Get-Dtc.md)

[Install-Dtc](./Install-Dtc.md)

[Start-Dtc](./Start-Dtc.md)

[Test-Dtc](./Test-Dtc.md)

[卸载 DTC](./Uninstall-Dtc.md)

